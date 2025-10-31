"""Spark demo analytics for the NYC taxi sample.

This is an example to showcase a Spark job on a Kubernetes cluster.
It reads the historical taxi CSV, curates a few helper columns, and emits four bite-sized tables that
are easy to verify during the demo run (trips per day, payment mix, busiest hours, and trip-length buckets).
"""
from typing import Optional

from pyspark.sql import SparkSession, functions as F, types as T


# explicit schema keeps Spark from doing an expensive header scan and guarantees consistent types
SCHEMA = T.StructType(
    [
        T.StructField("medallion", T.StringType(), False),
        T.StructField("hack_license", T.StringType(), False),
        T.StructField("pickup_datetime", T.StringType(), False),
        T.StructField("dropoff_datetime", T.StringType(), False),
        T.StructField("trip_time_in_secs", T.IntegerType(), False),
        T.StructField("trip_distance", T.DoubleType(), False),
        T.StructField("pickup_longitude", T.DoubleType(), False),
        T.StructField("pickup_latitude", T.DoubleType(), False),
        T.StructField("dropoff_longitude", T.DoubleType(), False),
        T.StructField("dropoff_latitude", T.DoubleType(), False),
        T.StructField("payment_type", T.StringType(), False),
        T.StructField("fare_amount", T.DoubleType(), False),
        T.StructField("surcharge", T.DoubleType(), False),
        T.StructField("mta_tax", T.DoubleType(), False),
        T.StructField("tip_amount", T.DoubleType(), False),
        T.StructField("tolls_amount", T.DoubleType(), False),
        T.StructField("total_amount", T.DoubleType(), False),
    ]
)


def prepare(df):
    """Parse timestamps, add helper columns, and drop obviously bad records."""
    pickup_ts = F.to_timestamp("pickup_datetime", "yyyy-MM-dd HH:mm:ss")
    return (
        df.withColumn("pickup_ts", pickup_ts)  # convert raw string into Spark timestamp
        .withColumn("pickup_date", F.to_date("pickup_ts"))
        .withColumn("pickup_hour", F.hour("pickup_ts"))
        .withColumn(
            "distance_bucket",
            F.when(F.col("trip_distance") < 1, "<1 mi")
            .when(F.col("trip_distance") < 3, "1-3 mi")
            .when(F.col("trip_distance") < 5, "3-5 mi")
            .when(F.col("trip_distance") < 10, "5-10 mi")
            .otherwise("10+ mi"),
        )
        .filter(F.col("pickup_ts").isNotNull())
        .filter(F.col("trip_distance") >= 0)  # drop telemetry glitches with impossible distances
        .filter(F.col("total_amount") >= 0)  # same for revenue values
    )


def save(df, root: str, name: str) -> None:
    """Persist a tiny CSV table in a deterministic location so the demo audience can inspect results."""
    df.coalesce(1).write.mode("overwrite").option("header", True).csv(f"{root}/{name}")


def main() -> Optional[int]:
    # 1. Use hard-coded parameters so the demo is entirely hands-off once launched
    input_path = "gs://assignment5bda/taxi-data-sorted-large.csv.bz2"  # e.g. local:///opt/spark/data/taxi-data-sorted-small.csv
    output_path = "gs://assignment5bda"  # e.g. s3a://my-bucket/taxi-output
    display_rows = 10
    # 2. Create or reuse a SparkSession; in Kubernetes this is done inside the driver pod
    spark = SparkSession.builder.appName("TaxiSparkK8sDemo").getOrCreate()
    try:
        # 3. Load the dataset with the fixed schema above
        raw_df = spark.read.csv(input_path, schema=SCHEMA)
        # 4. Apply lightweight cleansing/feature engineering once, cache for reuse
        taxi = prepare(raw_df).cache()
        taxi.count()  # materialize cache so subsequent actions run faster

        # --- Aggregation 1: Trips and revenue per day ---
        trips_per_day = (
            taxi.groupBy("pickup_date")
            .agg(
                F.count("*").alias("trip_count"),
                F.round(F.sum("total_amount"), 2).alias("total_revenue_usd"),
            )
            .orderBy("pickup_date")
        )
        trips_per_day.show(display_rows, truncate=False)
        save(trips_per_day, output_path, "trips_per_day")

        # --- Aggregation 2: Payment mix and tipping behavior ---
        payment_mix = (
            taxi.groupBy("payment_type")
            .agg(
                F.count("*").alias("trip_count"),
                F.round(F.mean("total_amount"), 2).alias("avg_total_usd"),
                F.round(F.mean("fare_amount"), 2).alias("avg_fare_usd"),
                F.round(F.mean(F.when(F.col("tip_amount") > 0, 1.0).otherwise(0.0)) * 100, 1).alias(
                    "pct_with_tip"
                ),
            )
            .orderBy(F.col("trip_count").desc())
        )
        payment_mix.show(display_rows, truncate=False)
        save(payment_mix, output_path, "payment_mix")

        # --- Aggregation 3: Demand by pickup hour ---
        busiest_hours = (
            taxi.groupBy("pickup_hour")
            .agg(
                F.count("*").alias("trip_count"),
                F.round(F.mean("fare_amount"), 2).alias("avg_fare_usd"),
            )
            .orderBy("pickup_hour")
        )
        busiest_hours.show(display_rows, truncate=False)
        save(busiest_hours, output_path, "busiest_hours")

        # --- Aggregation 4: Trip length buckets ---
        trip_lengths = (
            taxi.groupBy("distance_bucket")
            .agg(
                F.count("*").alias("trip_count"),
                F.round(F.mean("total_amount"), 2).alias("avg_total_usd"),
            )
            .orderBy(F.col("trip_count").desc())
        )
        trip_lengths.show(display_rows, truncate=False)
        save(trip_lengths, output_path, "trip_lengths")
    finally:
        # 5. Close the SparkSession so Kubernetes tears down the executor pods promptly
        spark.stop()
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

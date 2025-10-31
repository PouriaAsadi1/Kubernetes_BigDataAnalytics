"""Data Visualization.

Here we visualize the csv data that is produced from Spark. 
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df_busiest_hours = pd.read_csv('PATH TO busiest_hours CSV FILE')
df_payment_mix = pd.read_csv('PATH TO payment_mix CSV FILE')
df_trips_per_day = pd.read_csv('PATH TO trips_per_day CSV FILE')
df_trip_lengths = pd.read_csv('PATH TO trip_lengths CSV FILE')

# plot busiest hours
plt.figure(figsize=(10, 6))
plt.plot(df_busiest_hours['pickup_hour'], df_busiest_hours['trip_count'], marker='o')
plt.title('Busiest Hours for Taxi Trips')
plt.xlabel('Pickup Hour')
plt.ylabel('Number of Trips in Millions') 

# scale y-axis to millions
plt.ylim(0, df_busiest_hours['trip_count'].max() * 1.1)
yticks = plt.yticks()[0]
plt.yticks(yticks, [f'{int(y/1e6)}M' for y in yticks])
plt.grid()
plt.xticks(range(0, 24))
plt.savefig('busiest_hours.png')
plt.show()

# plot payment mix
# filter out NOC, UNK, and DIS for better x-axis labels
valid_payment_types = ['CRD', 'CSH']
df_payment_mix = df_payment_mix[df_payment_mix['payment_type'].isin(valid_payment_types)]
plt.figure(figsize=(10, 6))
plt.bar(df_payment_mix['payment_type'], df_payment_mix['trip_count'], color='skyblue')
plt.title('Payment Mix for Taxi Trips')
plt.xlabel('Payment Type')
plt.ylabel('Number of Trips in Millions')

# scale y-axis to millions
plt.ylim(0, df_payment_mix['trip_count'].max() * 1.1)
yticks = plt.yticks()[0]
plt.yticks(yticks, [f'{int(y/1e6)}M' for y in yticks])
plt.grid(axis='y')
plt.savefig('payment_mix.png')
plt.show()

# plot trips per day
plt.figure(figsize=(12, 6))
plt.plot(pd.to_datetime(df_trips_per_day['pickup_date']), df_trips_per_day['trip_count'], marker='o', color='orange')
plt.title('Trips Per Day')
plt.xlabel('Date')
plt.ylabel('Number of Trips in Thousands')

# scale y-axis to thousands
plt.ylim(0, df_trips_per_day['trip_count'].max() * 1.1)
yticks = plt.yticks()[0]
plt.yticks(yticks, [f'{int(y/1e3)}K' for y in yticks])
plt.grid()
plt.savefig('trips_per_day.png')
plt.show()

# plot trip lengths
plt.figure(figsize=(10, 6))
plt.bar(df_trip_lengths['distance_bucket'], df_trip_lengths['trip_count'], color='lightgreen')
plt.title('Trip Length Buckets')
plt.xlabel('Distance Bucket (miles)')
plt.ylabel('Number of Trips in Millions')

# scale y-axis to millions
plt.ylim(0, df_trip_lengths['trip_count'].max() * 1.1)
yticks = plt.yticks()[0]
plt.yticks(yticks, [f'{int(y/1e6)}M' for y in yticks])
plt.grid(axis='y')
plt.savefig('trip_lengths.png')
plt.show()
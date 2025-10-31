"""Data Visualization.

Here we visualize the csv data that is produced from Spark. 
"""

import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df_busiest_hours = pd.read_csv('/Users/pouriaasadi/busiest_hours/part-00000-a8fe8608-af72-427c-9c2d-dd8e18a2ad2f-c000.csv')
df_payment_mix = pd.read_csv('/Users/pouriaasadi/payment_mix/part-00000-129c17f1-2e08-4754-8f46-e32ddc8729d4-c000.csv')
df_trips_per_day = pd.read_csv('/Users/pouriaasadi/trips_per_day/part-00000-99ea6922-8c72-4a19-9e72-5420893bbd4a-c000.csv')
df_trip_lengths = pd.read_csv('/Users/pouriaasadi/trip_lengths/part-00000-90431d5e-cd0b-4e04-8d1f-e545fd1a48ac-c000.csv')

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
plt.ylabel('Number of Trips in Millions')

# scale y-axis to thousands
plt.ylim(0, df_trips_per_day['trip_count'].max() * 1.1)
yticks = plt.yticks()[0]
plt.yticks(yticks, [f'{int(y/1e3)}K' for y in yticks])
plt.grid()
plt.savefig('trips_per_day.png')
plt.show()
import pandas as pd
import folium
import numpy as np

# Read the CSV file
df = pd.read_csv('Locations.csv')

# Remove rows with NaN values in latitude or longitude
df = df.dropna(subset=['latitude', 'longitude'])

# Define the bounding box for Timor-Leste (approximate)
min_lat, max_lat = -9.5, -8.1
min_lon, max_lon = 124.0, 127.5

# Filter locations to keep only those within Timor-Leste
df = df[(df['latitude'] >= min_lat) & (df['latitude'] <= max_lat) &
        (df['longitude'] >= min_lon) & (df['longitude'] <= max_lon)]

# Create a map centered on Timor-Leste
m = folium.Map(location=[-8.8742, 125.7275], zoom_start=9, tiles='CartoDB positron')

# Add markers for each location
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        popup=row['name'],
        tooltip=row['name'],
        color='red',
        fill=True,
        fillColor='red'
    ).add_to(m)

# Add the bounding box to the map
folium.Rectangle(bounds=[[min_lat, min_lon], [max_lat, max_lon]], 
                 color="blue", weight=2, fill=False,
                 popup="Timor-Leste Bounding Box").add_to(m)

# Save the map
m.save('timor_leste_locations.html')

# Calculate distances and count reachable locations
def haversine_distance(lat1, lon1, lat2, lon2):
    from math import radians, sin, cos, sqrt, atan2
    R = 6371  # Earth's radius in kilometers

    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    a = sin(dlat/2)**2 + cos(lat1) * cos(lat2) * sin(dlon/2)**2
    c = 2 * atan2(sqrt(a), sqrt(1-a))
    distance = R * c

    return distance

def count_reachable_locations(df, movement_range=30):
    reachable_counts = []
    for index1, row1 in df.iterrows():
        count = 0
        for index2, row2 in df.iterrows():
            if index1 != index2:
                distance = haversine_distance(row1['latitude'], row1['longitude'], 
                                              row2['latitude'], row2['longitude'])
                if distance <= movement_range:
                    count += 1
        reachable_counts.append(count)
    return reachable_counts

reachable_counts = count_reachable_locations(df)

# Print statistics
total_locations = len(df)
locations_with_3_or_more = sum(1 for count in reachable_counts if count >= 3)
percentage = (locations_with_3_or_more / total_locations) * 100

print(f"Total locations: {total_locations}")
print(f"Locations with 3 or more reachable: {locations_with_3_or_more}")
print(f"Percentage: {percentage:.2f}%")

# Add reachable count to each marker
for index, row in df.iterrows():
    folium.CircleMarker(
        location=[row['latitude'], row['longitude']],
        radius=5,
        popup=f"{row['name']}<br>Reachable locations: {reachable_counts[index]}",
        tooltip=f"{row['name']} ({reachable_counts[index]})",
        color='red',
        fill=True,
        fillColor='red'
    ).add_to(m)

# Save the updated map
m.save('timor_leste_locations_with_counts.html')
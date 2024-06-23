import json
import geopandas as gpd
import pandas as pd
import numpy as np
import folium
from shapely.geometry import Point

# Load world dataset and filter for Timor-Leste
world = gpd.read_file(gpd.datasets.get_path('naturalearth_lowres'))
timor_leste = world[world.name == 'Timor-Leste']

# Load original locations from JSON
with open('timor_leste_locations.json', 'r') as f:
    original_locations = json.load(f)['locations']

# Convert original locations to GeoDataFrame
original_gdf = gpd.GeoDataFrame(
    original_locations,
    geometry=[Point(loc['longitude'], loc['latitude']) for loc in original_locations],
    crs="EPSG:4326"
)

# Generate random points within Timor-Leste
num_new_points = 50
new_points = []
while len(new_points) < num_new_points:
    minx, miny, maxx, maxy = timor_leste.total_bounds
    random_point = Point(np.random.uniform(minx, maxx), np.random.uniform(miny, maxy))
    if timor_leste.contains(random_point).any():
        new_points.append(random_point)

# Create GeoDataFrame for new points
new_gdf = gpd.GeoDataFrame(geometry=new_points, crs="EPSG:4326")
new_gdf['elevation'] = np.random.randint(0, 3000, size=len(new_gdf))

# Generate fantasy names for new locations
fantasy_words = ['Mystic', 'Enchanted', 'Whispering', 'Ethereal', 'Radiant', 'Shimmering', 'Thundering', 'Shadowy', 'Ancient', 'Forgotten', 'Celestial', 'Arcane', 'Mystical', 'Eldritch', 'Fabled']
fantasy_places = ['Grove', 'Cavern', 'Peak', 'Valley', 'Forest', 'River', 'Lake', 'Mountain', 'Ruins', 'Temple', 'Sanctuary', 'Oasis', 'Citadel', 'Glade', 'Haven']

new_gdf['name'] = [f"{np.random.choice(fantasy_words)} {np.random.choice(fantasy_places)} of Timor-Leste" for _ in new_gdf.geometry]

# Combine original and new locations
combined_gdf = pd.concat([original_gdf, new_gdf])

# Save to CSV
combined_gdf.to_csv('timor_leste_fantasy_locations.csv', index=False)

# Create a map
m = folium.Map(location=[-8.8742, 125.7275], zoom_start=9, tiles='CartoDB positron')

# Add Timor-Leste boundary
folium.GeoJson(timor_leste.geometry).add_to(m)

# Add markers for each location
for _, row in combined_gdf.iterrows():
    folium.CircleMarker(
        location=[row.geometry.y, row.geometry.x],
        radius=5,
        popup=f"{row['name']}<br>Elevation: {row['elevation']}m",
        tooltip=row['name'],
        color='red',
        fill=True,
        fillColor='red'
    ).add_to(m)

# Save the map
m.save('timor_leste_fantasy_locations_map.html')

print(f"Generated {len(combined_gdf)} locations in total.")
print("Saved locations to 'timor_leste_fantasy_locations.csv'")
print("Saved map to 'timor_leste_fantasy_locations_map.html'")
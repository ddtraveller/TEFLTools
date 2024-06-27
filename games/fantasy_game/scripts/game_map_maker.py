import json
import geopandas as gpd
import matplotlib.pyplot as plt
from shapely.geometry import Point, Polygon
from descartes import PolygonPatch

# Load the background data from the JSON file
with open("background_stories.json", "r") as file:
    background_data = json.load(file)

# Create a dictionary to store the coordinates of each place
place_coordinates = {
    "Zephyr Mountains": (0.3, 0.7),
    "Zephyria": (0.6, 0.8),
    "Whispering Winds": (0.2, 0.6),
    "Emberveld": (0.8, 0.4),
    "Emberfell": (0.7, 0.2),
    "Crimson Steppes": (0.5, 0.3),
    "Blaze Peaks": (0.9, 0.6),
    "Cinderwood": (0.4, 0.1),
    "Sapphire Isles": (0.1, 0.9),
    "Emerald Isles": (0.2, 0.8),
    "Cerulean Coast": (0.1, 0.2),
    "Emerald Vale": (0.6, 0.6),
    "Emerald Kingdom": (0.7, 0.7),
    "Whispering Woods": (0.3, 0.4),
    "Verdant Spires": (0.5, 0.5)
}

# Create a list of polygons representing the fantasy regions
regions = [
    Polygon([(0, 0), (0.5, 0), (0.5, 0.5), (0, 0.5)]),
    Polygon([(0.5, 0), (1, 0), (1, 0.5), (0.5, 0.5)]),
    Polygon([(0, 0.5), (0.5, 0.5), (0.5, 1), (0, 1)]),
    Polygon([(0.5, 0.5), (1, 0.5), (1, 1), (0.5, 1)])
]

# Create a GeoDataFrame with the regions
gdf = gpd.GeoDataFrame(geometry=regions)

# Create a figure and axis
fig, ax = plt.subplots(figsize=(10, 10))

# Plot the fantasy regions
for region in gdf.geometry:
    patch = PolygonPatch(region, facecolor='lightgreen', edgecolor='black', linewidth=2)
    ax.add_patch(patch)

# Iterate over each background story
for background in background_data["backgrounds"]:
    # Extract the place name from the story
    for place, coordinates in place_coordinates.items():
        if place in background["story"]:
            # Create a marker for the place
            ax.plot(coordinates[0], coordinates[1], 'bo', markersize=10)
            ax.text(coordinates[0], coordinates[1], place, fontsize=12, ha='center', va='bottom')

# Remove the axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.axis('off')

# Set the title of the map
ax.set_title("Fantasy World Map", fontsize=16)

# Display the map
plt.tight_layout()
plt.savefig('map.png')
plt.show()
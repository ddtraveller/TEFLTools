import folium
from folium.plugins import MarkerCluster
import json

# Load data from JSON file
with open('timor_leste_minerals.json', 'r') as f:
    data = json.load(f)

# Create a map object centered on Timor-Leste
map_timor_leste = folium.Map(location=[-8.8, 125.7], zoom_start=8, tiles='OpenStreetMap')

# Define colors for each resource type
colors = {
    'Copper': 'red',
    'Gold': 'orange',
    'Manganese': 'purple',
    'Chromite': 'gray',
    'Limestone': 'blue',
    'Marble': 'green',
    'Bentonite': 'pink',
    'Phosphate': 'cadetblue'
}

# Create MarkerClusters for each resource type
clusters = {}
for resource in data['resources']:
    clusters[resource] = MarkerCluster(name=resource, overlay=True, control=True, show=True)

# Plot the resources on the map
for resource, locations in data['resources'].items():
    for location_data in locations:
        folium.Marker(
            location_data['location'],
            popup=f"{resource} - {location_data['name']}",
            icon=folium.Icon(color=colors[resource], icon='gem', prefix='fa')
        ).add_to(clusters[resource])

# Add clusters to map
for cluster in clusters.values():
    cluster.add_to(map_timor_leste)

# Add a custom legend
legend_html = """
<div style="position: fixed; bottom: 50px; left: 50px; width: 150px; 
    border:2px solid grey; z-index:9999; font-size:14px; background-color:white;
    padding: 10px;
    ">
    <strong>Mineral Resources</strong><br>
"""
for resource, color in colors.items():
    legend_html += f'<i class="fa fa-gem fa-1x" style="color:{color}"></i> {resource}<br>'
legend_html += "</div>"
map_timor_leste.get_root().html.add_child(folium.Element(legend_html))

# Add layer control
folium.LayerControl().add_to(map_timor_leste)

# Save the map
map_timor_leste.save("timor_leste_minerals_map.html")
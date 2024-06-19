import folium
from folium.plugins import HeatMap
import random
from branca.colormap import LinearColormap

# Create a base map centered on a specific location
map_center = [-8.5557, 125.5135]  # Coordinates for Timor-Leste
site_map = folium.Map(location=map_center, zoom_start=8)

# Add a marker for the site location
folium.Marker(map_center, popup='Permaculture Site', icon=folium.Icon(color='green')).add_to(site_map)

# Create feature groups for each layer
soil_types_group = folium.FeatureGroup(name='Soil Types')
water_sources_group = folium.FeatureGroup(name='Water Sources')
sun_exposure_group = folium.FeatureGroup(name='Sun Exposure')

# Add colored areas representing different soil types
soil_types = [
    {'name': 'Sandy Loam', 'color': 'orange'},
    {'name': 'Clay Loam', 'color': 'darkred'},
    {'name': 'Silt Loam', 'color': 'darkblue'}
]

for soil_type in soil_types:
    coordinates = [
        [-8.6 + random.uniform(-0.1, 0.1), 125.4 + random.uniform(-0.1, 0.1)],
        [-8.6 + random.uniform(-0.1, 0.1), 125.6 + random.uniform(-0.1, 0.1)],
        [-8.4 + random.uniform(-0.1, 0.1), 125.6 + random.uniform(-0.1, 0.1)],
        [-8.4 + random.uniform(-0.1, 0.1), 125.4 + random.uniform(-0.1, 0.1)]
    ]
    folium.Polygon(coordinates, color=soil_type['color'], popup=soil_type['name']).add_to(soil_types_group)

# Add points of interest representing water sources
water_sources = [
    {'name': 'Spring', 'coordinates': [-8.55, 125.52], 'icon': 'tint', 'color': 'blue'},
    {'name': 'Stream', 'coordinates': [-8.58, 125.55], 'icon': 'tint', 'color': 'darkblue'}
]

for source in water_sources:
    folium.Marker(source['coordinates'], popup=source['name'], icon=folium.Icon(icon=source['icon'], prefix='fa', color=source['color'])).add_to(water_sources_group)

# Add a heat map representing sun exposure
heat_data = [
    [-8.55 + random.uniform(-0.05, 0.05), 125.52 + random.uniform(-0.05, 0.05), random.randint(0, 1000)]
    for _ in range(100)
]
HeatMap(heat_data, name='Sun Exposure').add_to(sun_exposure_group)

# Add the feature groups to the map
soil_types_group.add_to(site_map)
water_sources_group.add_to(site_map)
sun_exposure_group.add_to(site_map)

# Add a layer control to toggle the visibility of the feature groups
folium.LayerControl().add_to(site_map)

# Create a legend for soil types
soil_legend_html = '''
<div style="position: fixed; bottom: 50px; left: 50px; width: 150px; height: 105px; border:2px solid grey; z-index:9999; font-size:12px; background-color: white; overflow: auto;">
    &nbsp;<b>Soil Types</b><br>
    &nbsp;<span style="color:orange; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;Sandy Loam<br>
    &nbsp;<span style="color:darkred; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;Clay Loam<br>
    &nbsp;<span style="color:darkblue; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;Silt Loam<br>
</div>
'''

# Create a legend for water sources
water_legend_html = '''
<div style="position: fixed; bottom: 50px; left: 200px; width: 150px; height: 75px; border:2px solid grey; z-index:9999; font-size:12px; background-color: white; overflow: auto;">
    &nbsp;<b>Water Sources</b><br>
    &nbsp;<span style="color:blue; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;Spring<br>
    &nbsp;<span style="color:darkblue; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;Stream<br>
</div>
'''

# Create a legend for water sources
heat_map_legend_html = '''
<div style="position: fixed; bottom: 50px; left: 350px; width: 150px; height: 75px; border:2px solid grey; z-index:9999; font-size:12px; background-color: white; overflow: auto;">
    &nbsp;<b>Heat Map</b><br>
    &nbsp;<span style="color:Red; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;40c<br>
    &nbsp;<span style="color:Orange; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;37c<br>
    &nbsp;<span style="color:Yellow; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;34c<br>
    &nbsp;<span style="color:Green; font-weight:bold; font-size:14px;">&nbsp;&bull;</span>&nbsp;31c<br>
</div>
'''

# Create a title for the map
title_html = '''
<div style="position: fixed; top: 10px; left: 50px; width: 500px; height: 75px; border:2px solid grey; z-index:9999; font-size:14px; background-color: white; overflow: auto;">
    &nbsp;<h3>Permaculture Site Assessment Map - Timor-Leste</h3>
    &nbsp;<p>This map illustrates the various factors considered for permaculture design, including soil types, water sources, and sun exposure.</p>
</div>
'''

# Add the legends and title to the map
site_map.get_root().html.add_child(folium.Element(soil_legend_html))
site_map.get_root().html.add_child(folium.Element(water_legend_html))
site_map.get_root().html.add_child(folium.Element(heat_map_legend_html))
site_map.get_root().html.add_child(folium.Element(title_html))

# Display the map
site_map.save('permaculture_site_map.html')
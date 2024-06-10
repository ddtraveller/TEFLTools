import folium

# Create a map centered on Dili
dili_map = folium.Map(location=[-8.5579, 125.5736], zoom_start=13)

# Add markers for vacant buildings
folium.Marker(
    [-8.5628, 125.5688],
    popup="Vacant Building",
    icon=folium.Icon(color="gray")
).add_to(dili_map)

folium.Marker(
    [-8.5549, 125.5721],
    popup="Vacant Building",
    icon=folium.Icon(color="gray")
).add_to(dili_map)

# Add markers for convenience stores
folium.Marker(
    [-8.5602, 125.5757],
    popup="Convenience Store",
    icon=folium.Icon(color="green")
).add_to(dili_map)

folium.Marker(
    [-8.5518, 125.5701],
    popup="Convenience Store",
    icon=folium.Icon(color="green")
).add_to(dili_map)

# Add markers for gas stations
folium.Marker(
    [-8.5644, 125.5712],
    popup="Gas Station",
    icon=folium.Icon(color="red")
).add_to(dili_map)

# Add markers for risky places
folium.Marker(
    [-8.5582, 125.5668],
    popup="Risky Place",
    icon=folium.Icon(color="black")
).add_to(dili_map)

# Add a legend
legend_html = """
<div style="position: fixed; bottom: 50px; left: 50px; width: 140px; border:2px solid grey; z-index:9999; font-size:14px; background-color: white; padding: 10px;">
<p style="margin: 0;"><span style="color: gray">&#9679;</span> Vacant Building</p>
<p style="margin: 0;"><span style="color: green">&#9679;</span> Convenience Store</p>
<p style="margin: 0;"><span style="color: red">&#9679;</span> Gas Station</p>
<p style="margin: 0;"><span style="color: black">&#9679;</span> Risky Place</p>
</div>
"""
dili_map.get_root().html.add_child(folium.Element(legend_html))

# Save the map as an HTML file
dili_map.save("dili_map.html")
import folium
import h3

# config
gpxpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
outpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-out/"


delhi_cell = h3.latlng_to_cell(28.6139, 77.2090, 12)  # New Delhi coordinates

# Traverse hierarchy upwards
parent = h3.cell_to_parent(delhi_cell, res=11)
print(f"Parent at res 8: {parent}")

# Traverse hierarchy downwards
children = h3.cell_to_children(parent, res=13)
print(f"Contains {len(children)} children")

# Create a new map centered on New Delhi
delhi_map = folium.Map(location=[28.6139, 77.2090], zoom_start=15)

# Add the parent hexagon (resolution 8)
folium.Polygon(
    locations= h3.cell_to_boundary(parent),
    color='red',
    fill=True,
    weight=2,
    popup=f'Parent: {parent}'
).add_to(delhi_map)

# Add all children hexagons (resolution 9)
for child_cell in children:
    color = 'yellow' if child_cell == delhi_cell else 'blue'
    folium.Polygon(
        locations= h3.cell_to_boundary(child_cell),
        color=color,
        fill=True,
        weight=1,
        popup=f'Child: {child_cell}'
    ).add_to(delhi_map)

delhi_map.save(outpath + "test9.html")
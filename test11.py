# This is to test the resolution and levels of H3
import folium
import h3

# config
inpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
outpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-out/"


seattle_cell = h3.latlng_to_cell(47.604566, -122.332371, 12)  # Seattle coordinates


# Traverse hierarchy upwards
parent = h3.cell_to_parent(seattle_cell, res=11)
print(f"Parent at res 8: {parent}")

# Traverse hierarchy downwards
children = h3.cell_to_children(parent, res=13)
print(f"Contains {len(children)} children")

# Create a new map centered on New seattle
seattle_map = folium.Map(location=[47.604566, -122.332371], zoom_start=15)

# Add the parent hexagon (resolution 8)
folium.Polygon(
    locations= h3.cell_to_boundary(parent),
    color='red',
    fill=True,
    weight=2,
    popup=f'Parent: {parent}'
).add_to(seattle_map)

# Add all children hexagons (resolution 9)
for child_cell in children:
    color = 'yellow' if child_cell == seattle_cell else 'blue'
    folium.Polygon(
        locations= h3.cell_to_boundary(child_cell),
        color=color,
        fill=True,
        weight=1,
        popup=f'Child: {child_cell}'
    ).add_to(seattle_map)

seattle_map.save(outpath + "test11.html")
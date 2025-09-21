# This is to test the resolution and levels of H3
import folium
import h3

# config
inpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
outpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-out/"
lat = 47.604566 # Seattle
long = -122.332371
latlong = 47.604566, -122.332371
init_res = 14
up = 4

latlong_cell = h3.latlng_to_cell(lat,long, init_res)


# Create a new map centered on latlong
map = folium.Map(location=[lat, long], zoom_start=init_res)

parent = h3.cell_to_parent(latlong_cell, init_res)

# Traverse hierarchy downwards
children = h3.cell_to_children(parent, init_res)
print(f"Contains {len(children)} children")

# Add all children hexagons
for child_cell in children:
    color = 'yellow' if child_cell == latlong_cell else 'blue'
    folium.Polygon(
        locations= h3.cell_to_boundary(child_cell),
        color=color,
        fill=True,
        weight=1,
        popup=f'Child: {child_cell}'
    ).add_to(map)

# Traverse hierarch up 
loop_res = init_res
for i in range(up):
    # Code to be executed in each iteration
    loop_res = loop_res - 1
    print(f"This is iteration {i + 1}")
    print (f"Resolution: {loop_res}")
    parent = h3.cell_to_parent(latlong_cell, loop_res)
    # Add the parent hexagon
    folium.Polygon(
        locations= h3.cell_to_boundary(parent),
        color='red',
        fill=True,
        weight=2,
        popup=f'Parent: {parent} res: {loop_res}'
    ).add_to(map)

map.save(outpath + "test12.html")
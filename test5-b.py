import geopandas as gpd
import pyarrow
import os
import matplotlib.pyplot as plt
import fiona
from fiona import Geometry, Feature, Properties

# config
gpx_path = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
out_path = "/Users/tim/DocumentsLocal/Github/cdmx25/data-out/"
# testplt_gpx = plt.subplots()

# Read the GPX file
gpx_file = (gpx_path + "LuckyLake.gpx")
outfile_root = "LuckyLake"

# List available layers
layers = fiona.listlayers(gpx_file)
# Filter for only non-empty layers
non_empty_layers = []

for layer in layers:
    try:
        gdf = gpd.read_file(gpx_file, layer=layer)
        print(f"Layer '{layer}' contains {len(gdf)} features.")
        if not gdf.empty:
            non_empty_layers.append(layer)
            outfile = str(out_path + outfile_root + "-" + layer + "-" + ".geojson")
            gdf.to_file(outfile, driver='GeoJSON')
    except Exception as e:
        print(f"Error reading layer '{layer}': {e}")

print("Available layers:", layers)
print("Non-empty layers:", non_empty_layers)
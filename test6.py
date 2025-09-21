import geopandas as gpd
import pandas as pd
import pyarrow
import os
import matplotlib.pyplot as plt
import fiona
from fiona import Geometry, Feature, Properties

# config
gpx_path = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
# change the global options that Geopandas inherits from
pd.set_option('display.max_columns',None)

# testplt_gpx = plt.subplots()

# Read the GPX file
gpx_file = (gpx_path + "LuckyLake.gpx")

# List available layers
layers = fiona.listlayers(gpx_file)
# Filter for only non-empty layers
non_empty_layers = []

for layer in layers:
    try:
        gdf = gpd.read_file(gpx_file, layer=layer)
        gdf = gdf.dropna(axis=1, how='all')
        if not gdf.empty:
            non_empty_layers.append(layer)
            print("All Columns: " , gdf.columns)
            # Drop empty columns
            gdf = gdf.dropna(axis=1, how='all')
            print("Trimmed Columns: ", gdf.columns)
    except Exception as e:
        print(f"Error reading layer '{layer}': {e}")

print("Available layers:", layers)
print("Non-empty layers:", non_empty_layers)
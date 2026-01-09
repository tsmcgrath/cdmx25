# this is going to write it to geoparquet via duckdb
import os
import duckdb
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
import pyarrow
import matplotlib.pyplot as plt
import fiona
from fiona import Geometry, Feature, Properties

# Subprocess example:
import subprocess
result = subprocess.run(
    ["ls", "-la"],
    capture_output=True,
    text=True,
    check=True
)
print(result.stdout)

# Use pathlib
from pathlib import Path
logs = Path("logs")
for file in logs.glob("*.txt"):
    print(file.name)

# Use loguru
from loguru import logger
logger.add("automation.log")
logger.info("Task started")

# config
gpx_path = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
outpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-out/"
# change the global options that Geopandas inherits from
pd.set_option('display.max_columns',None)

# testplt_gpx = plt.subplots()

# Read the GPX file
gpx_file = (gpx_path + "LuckyLake.gpx")
parquet_file = (outpath + "LuckyLake.parquet")

# List available layers
layers = fiona.listlayers(gpx_file)
# Filter for only non-empty layers
non_empty_layers = []

for layer in layers:
    try:
        gdf = gpd.read_file(gpx_file, layer=layer)
        empty_cols = gdf.columns[gdf.isna().all()]
        print("Empty columns:", list(empty_cols))
        if not gdf.empty:
            non_empty_layers.append(layer)
            outfile = str(outpath + "-" + layer + ".geojson")
            # Drop columns where *any* value is null
            gdf_cleaned = gdf.dropna(axis=1, how='any')
            gdf = gpd.GeoDataFrame(gdf_cleaned, crs="EPSG:4326")
            print(gdf.head())
            print(gdf.crs)
            print(gdf.dtypes)
            print(gdf.columns)
    except Exception as e:
        print(f"Error reading layer '{layer}': {e}")



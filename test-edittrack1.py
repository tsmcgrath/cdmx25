import pandas as pd
import geopandas as gpd
import pyarrow
import os
import matplotlib.pyplot as plt
import fiona
from fiona import Geometry, Feature, Properties
from datetime import datetime, UTC
from zoneinfo import ZoneInfo

# config
gpx_path = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
out_path = "/Users/tim/DocumentsLocal/Github/cdmx25/data-out/"
# 1. Create a ZoneInfo object for Mexico City
mexico_city_tz = ZoneInfo('America/Mexico_City')
# testplt_gpx = plt.subplots()

# Read the GPX file
gpx_file = (gpx_path + "TacoRide.gpx")
outfile_root = "TacoRide-edited"

# List available layers
layers = fiona.listlayers(gpx_file)
# Filter for only non-empty layers
non_empty_layers = []

for layer in layers:
    try:
        gdf = gpd.read_file(gpx_file, layer=layer)
        print("CRS: " + str(gdf.crs))
        print(f"Layer '{layer}' contains {len(gdf)} features.")
        if not gdf.empty:
            non_empty_layers.append(layer)
            outfile = str(out_path + outfile_root + "-" + layer + ".geojson")
            # Drop columns where *any* value is null
            gdf_cleaned = gdf.dropna(axis=1, how='any')
            # Convert UTC time to local time
            gdf_cleaned['local-dtime'] = pd.to_datetime(gdf_cleaned['time'])
            gdf_cleaned['local-dtime'] = gdf_cleaned['local-dtime'].dt.tz_convert(mexico_city_tz)
            # Output GeoJson
            gdf_cleaned.to_file(outfile, driver='GeoJSON')
    except Exception as e:
        print(f"Error reading layer '{layer}': {e}")

print("Available layers:", layers)
print("Non-empty layers:", non_empty_layers)
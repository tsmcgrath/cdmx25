import geopandas as gpd
import os
import matplotlib.pyplot as plt

# config
gpxpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data/"
testplt_gpx = plt.subplots()

# Read the GPX file
gpx_file = (gpxpath + "TacoRide.gpx")

# List available layers
layers = fiona.listlayers(gpx_path)
print("Available layers:", layers)

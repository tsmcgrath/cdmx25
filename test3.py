# Fails. Abandoned.
# # from the readme at: https://github.com/FABallemand/ezGPX

import ezgpx
from ezgpx import GPX
from geojson_transformer import GeoJsonTransformer
import matplotlib.pyplot as plt


# config
gpxpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data/"
#testplt_gpx = plt.subplots()
# Parse GPX file
gpxfile = ezgpx.GPX(gpxpath + "TacoRide.gpx")
gpxfile = GeoJsonTransformer(path=(gpxpath + "TacoRide.gpx"), output_path=(gpxpath + "TacoRide.geojson"))


# Retrieve start/stop time
start_time = gpx.start_time()
stop_time = gpx.stop_time()
print(f"Start time: {start_time}, Stop time: {stop_time}")

# Compute the total amount of time elapsed
elapsed_time = gpx.total_elapsed_time()
print(f"Total elapsed time: {elapsed_time}")

# Compute the total amount of time stopped
stopped = gpx.stopped_time()
print(f"Total stopped time: {stopped}")

# Compute the total amount of time spent moving
moving_time = gpx.moving_time()
print(f"Total moving time: {moving_time}")

print("GeoJSON file created successfully.","\n",gjfile)

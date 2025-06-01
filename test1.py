# from the readme at: https://github.com/FABallemand/ezGPX

import ezgpx
import matplotlib.pyplot as plt


# config
gpxpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data/"
testplt_gpx = plt.subplots()
# Parse GPX file
newgpx = ezgpx.GPX(gpxpath + "TacoRide.gpx")

# Simplify (using Ramer-Dougle-Peucker algorithm)
newgpx.simplify()

# Remove metadata
newgpx.remove_metadata()

# Write new simplified GPX file
newgpx.to_gpx(gpxpath + "new_TacoRide.gpx")
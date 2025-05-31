# from the readme at: https://github.com/FABallemand/ezGPX

import ezgpx
import matplotlib


# config
gpxpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data/"

# Parse GPX file
gpx = ezgpx.GPX(gpxpath + "activity_18627254105.gpx")

# Simplify (using Ramer-Dougle-Peucker algorithm)
gpx.simplify()

# Remove metadata
gpx.remove_metadata()

# Plot with Matplotlib
test_gpx.matplotlib_plot(figsize=(16,9),
                         size=6,
                         color="ele",
                         cmap=matplotlib.cm.get_cmap("gnuplot", 12),
                         colorbar=False,
                         start_point_color="green",
                         stop_point_color="red",
                         way_points_color=None,
                         background="World_Imagery",
                         offset_percentage=0.04,
                         dpi=100,
                         title=test_gpx.name(),
                         title_fontsize=20,
                         watermark=True,
                         file_path="img_1.png")

# Write new simplified GPX file
gpx.to_gpx(gpxpath + "new_file.gpx")
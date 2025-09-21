import folium

# config
gpxpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-in/"
outpath = "/Users/tim/DocumentsLocal/Github/cdmx25/data-out/"

m = folium.Map(location=(45.5236, -122.6750))

m.save(outpath + "test10.html")
from arcgis.gis import GIS
from getpass import getpass

# i'm using the `getpass` library here but you can hard-code your u/p if you like
username = getpass('Username: ')
password = getpass()
arcgis_url = 'https://www.arcgis.com'

# create your `gis` instance 
gis = GIS(arcgis_url, username, password)

# where is the incoming GeoJson file?
in_geojson = './merged_file.geojson'

# add the GeoJson file to your account
print ('adding GeoJson file to your ArcGIS Online account..')

# special note of how the `type` property is `GeoJson` 
# an odd choice of spelling and we don't really doc this explictly
item_properties = {
  'title': 'some title',
  'tags': 'some, tags',
  'type': 'GeoJson'
}
geojson_item = gis.content.add(item_properties, in_geojson)

# publish GeoJson Item as a hosted Feature Service
print ('publishing GeoJson as a hosted feature service ..')
geojson_item.publish()

print ('done')
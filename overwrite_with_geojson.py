from arcgis.gis import GIS
from arcgis.features import FeatureLayerCollection
from getpass import getpass

# i'm using the `getpass` library here but you can hard-code your u/p if you like
username = getpass('Username: ')
password = getpass()
arcgis_url = 'https://www.arcgis.com'

# create your `gis` instance 
gis = GIS(arcgis_url, username, password)

# get the Item to be updated/overwritten by Item ID
item_id = '7067340a894f4e818e880a5f52cd15e4'
item = gis.content.get(item_id)

# create a FLC from the item to do the overwrite
flc = FeatureLayerCollection.fromitem(item)

# do the overwrite
print ('overwriting with new data ..')
new_data = './sample_points.geojson'
flc.manager.overwrite(new_data)

print ('done')
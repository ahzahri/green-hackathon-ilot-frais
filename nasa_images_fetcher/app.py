from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import ee
import json
import sys

# get all other input from command lines args
# we start with the latitude adn the longitude
# 48.54699732502393, 7.769870971824026 => example location of the CyberGrange
lat = sys.argv[1]
lon = sys.argv[2]

# get date of the imagery
# if no date provided, we get the start of previous month in format YYYY-MM-DD
date = (datetime.today() - relativedelta(months=1)).strftime('%Y-%m-%d')
if (len(sys.argv) == 4):
    date = sys.argv[3]
print("Date of imagery: " + date)

# Load the service account credentials.
service_account = 'earth-engine-fetcher@ilot-frais.iam.gserviceaccount.com'
credentials = ee.ServiceAccountCredentials(service_account, 'earth-engine-fetcher_sa.json')

# Initialize the Earth Engine module.
ee.Initialize(credentials)

# Define a region of interest as a Point.
point = ee.Geometry.Point(lon=float(lon), lat=float(lat))  # Strasbourg

# Define the image collection
collection = ee.ImageCollection('LANDSAT/LC08/C01/T1_SR')\
    .filterBounds(point)\
    .filterDate((datetime.strptime(date, '%Y-%m-%d') - relativedelta(months=1)).strftime('%Y-%m-%d'), date)\
    .sort('CLOUD_COVER', True) # sort by cloud cover ascending

# Get the least cloudy image.
image = ee.Image(collection.first())
# we copy the image data output to a file first
if (image is not None):
    json_file_path = "./json/ee_data_" + datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".json"
    with open(json_file_path, 'w') as outfile:
        json.dump(image.getInfo(), outfile)
else:
    print("No data fetched from NASA API")

# Get the URL of a thumbnail image
url = image.getThumbURL({
    'bands': ['B4', 'B3', 'B2'],  # RGB
    'min': 0,
    'max': 3000,
    'dimensions': 1024
})

print(url)

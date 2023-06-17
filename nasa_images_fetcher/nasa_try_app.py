from datetime import datetime
from dateutil.relativedelta import relativedelta
from dotenv import load_dotenv
import json
import os
import requests
import sys

# loading the environment variables from the .env file
load_dotenv(dotenv_path='/home/images_fetcher/app/.env')

def fetch_nasa_data(api_key, lon, lat, date):
    base_url = "https://api.nasa.gov/planetary/earth/assets?"
    params = {
        "lon": lon,
        "lat": lat,
        "date": date, # beginning of 30 day date range that will be used to look for closest image to that date
        "api_key": api_key,
    }
    response = requests.get(base_url, params=params)
    if response.status_code == 200:
        return response.json()
    else:
        return None

# get the API key from an environment variable
api_key = os.getenv('NASA_API_KEY', None)

# Check that the correct number of arguments was provided
if len(sys.argv) < 2:
    print("You must provide exactly 2 arguments :longitude and latitude (in that order), one optional argument is date")
    sys.exit(1)

# get all other input from command lines args
# we start with the longitude and latitude
# 48.54699732502393, 7.769870971824026 => example location of the CyberGrange
lon = sys.argv[1]
lat = sys.argv[2]

# get date of the imagery
# if no date provided, we get the start of previous month in format YYYY-MM-DD
date = (datetime.today() - relativedelta(months=1)).strftime('%Y-%m-%d')
if (len(sys.argv) == 4):
    date = sys.argv[3]
print("Date of imagery: " + date)

data = fetch_nasa_data(api_key, lon, lat, date)

# we copy the JSON output to a file first
if (data is not None):
    json_file_path = "./json/nasa_data_" + datetime.now().strftime("%Y-%m-%d_%H:%M:%S") + ".json"
    with open(json_file_path, 'w') as outfile:
        json.dump(data, outfile)
else:
    print("No data fetched from NASA API")

# TODO write the output to a CSV file


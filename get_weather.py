# importing the requests library
import requests
import sys

# api-endpoint
URL = "https://api.openweathermap.org/data/2.5/onecall"

# parameters
latitude = "43.161030"
longitude = "-77.610924"
exclude = "minutely,daily,current"
units="Imperial"

if len(sys.argv) < 2:
    print("Usage: python get_weather.py {OPEN_WEATHER_API_KEY}")
    sys.exit(0)

apiKey = sys.argv[1]

PARAMS = {'lat':latitude, 'lon':longitude, 'exclude':exclude, 'units':units, 'appid': apiKey}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

print(data)
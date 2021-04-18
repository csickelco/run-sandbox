# importing the requests library
import requests
from datetime import datetime
from dateutil import tz

to_zone = tz.gettz('America/New_York')

#Constants
ISO_8601_FORMAT = "%Y-%m-%dT%H:%M:%S%z"

# api-endpoint
URL = "https://api.sunrise-sunset.org/json"

# parameters
latitude = "43.161030"
longitude = "-77.610924"
dateVal = "tomorrow"

PARAMS = {'lat':latitude, 'lng':longitude, 'date':dateVal, 'formatted': 0}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

# extracting sunrise, civil_twilight_begin
sunriseUTC = datetime.strptime(data['results']['sunrise'], ISO_8601_FORMAT)
sunriseLocal = sunriseUTC.astimezone(to_zone)
civilTwilightBeginUTC = datetime.strptime(data['results']['civil_twilight_begin'], ISO_8601_FORMAT)
civilTwilightBeginLocal = civilTwilightBeginUTC.astimezone(to_zone)

# printing the output
print(f'sunrise: {sunriseLocal.time()}\ntwilight_begin: {civilTwilightBeginLocal.time()}')
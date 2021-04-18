# importing the requests library
import requests

# api-endpoint
URL = "https://api.sunrise-sunset.org/json"

# parameters
latitude = "43.161030"
longitude="-77.610924"
dateVal="tomorrow"

PARAMS = {'lat':latitude, 'lng':longitude, 'date':dateVal}

# sending get request and saving the response as response object
r = requests.get(url=URL, params=PARAMS)

# extracting data in json format
data = r.json()

# extracting sunrise, civil_twilight_begin
sunrise = data['results']['sunrise']
civilTwilightBegin = data['results']['civil_twilight_begin']

# printing the output
print(f'sunrise: {sunrise}, twilight_begin: {civilTwilightBegin}')
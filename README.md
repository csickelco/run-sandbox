# Setup

1. Install python 3.9.4 and pip3
2. git clone git@github.com:csickelco/run-sandbox.git
3. pip install -r requirements.txt OR (to upgrade) pip install --upgrade -r requirements.txt

# Maintenance
pip freeze > requirements.txt

# APIs

## Sunrise and Sunset
https://sunrise-sunset.org/api

curl -X GET "https://api.sunrise-sunset.org/json?lat=43.161030&lng=-77.610924&date=tomorrow"


## Weather
https://openweathermap.org/api/one-call-api

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

https://api.openweathermap.org/data/2.5/onecall?lat={lat}&lon={lon}&exclude={part}&units=Imperials&appid={API key}

curl -X GET https://api.openweathermap.org/data/2.5/onecall?lat=43.161030&lon=-77.610924&exclude=minutely,daily&appid={API key}

Response fields:
* hourly.dt: date/time in UTC
* hourly.temp: temperature in fahrenheit
* hourly.feels_like: temperature in fahrenheit. This accounts for the human perception of weather.
* hourly.wind_speed: wind speed in miles/hour
* hourly.wind_gust: wind gusts in miles/hour
* hourly.rain.1h: rain volume in mm for last hour
* hourly.snow.1h: snow volume in mm for last hour
* hourly.weather.main: Group of weather parameters (Rain, Snow, Extreme etc.)
* hourly.weather.description: Full weather conditions, see https://openweathermap.org/weather-conditions#Weather-Condition-Codes-2
 
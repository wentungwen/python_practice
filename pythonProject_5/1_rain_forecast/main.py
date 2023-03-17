import requests
import os
from twilio.rest import Client


account_sid = "ACe6490eed28972d424c82ed31132d1755"
auth_token = "211a2952d250edcb9e832cd8b09d2884"
OWN_Endpoint = "http://api.weatherapi.com/v1/forecast.json"
api_key = "2c5ef5defc054660906183401231303"
params = {
    "key": api_key,
    "q": "Tilburg",
    "days": 3,
    "aqi": "no",
    "alerts": "no",
    "forecastday": "hour"
}

res_code = requests.get("https://www.weatherapi.com/docs/weather_conditions.json").json()
rain_code = [n["code"] for n in res_code if 1180 < n["code"] < 1201]
res = requests.get(OWN_Endpoint, params=params)
data = res.json()["forecast"]["forecastday"]
hourly_code = [hour["condition"]["code"] for day in data for hour in day["hour"][9:]]
is_rain = False

for n in hourly_code:
    if n in rain_code:
        is_rain = True

if is_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
      body="Bring umbrella!",
      from_="+15073846093",
      to="+31619013911"
    )
    print(message.status)





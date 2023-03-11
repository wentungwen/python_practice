import requests
import datetime as dt

MY_LAT = 36.7201600
MY_LNG = -4.4203400

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json", params=params)
response.raise_for_status()
data = response.json()
sunrise = data["results"]["sunrise"]
sunset = data["results"]["sunset"]
sunrise_hour = sunrise.split("T")[1].split(":")[0:2]
print(sunrise)
print(sunrise_hour)

time_now = dt.datetime.now()
print(time_now)



import requests
from datetime import datetime
import smtplib


MY_LAT = 42.262592
MY_LONG = -71.802292
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400", params=parameters)
response.raise_for_status()
sunrise = response.json()["results"]["sunrise"]
sunset = response.json()["results"]["sunset"]
print(response.json())
print(sunrise.split("T")[1].split(":")[0])
print(sunset.split("T")[1].split(":")[0])
time_now = datetime.now()
print(time_now.hour)

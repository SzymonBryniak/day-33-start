import requests
from datetime import datetime
import smtplib
import time

MY_LAT = 42.262592
MY_LONG = -71.802292
parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0
}

response_weather = requests.get("https://api.sunrise-sunset.org/json?lat=36.7201600&lng=-4.4203400", params=parameters)
response_weather.raise_for_status()
# response_iss = requests.get(url="http://api.open-notify.org/iss-now.json")
# response_iss.raise_for_status()

sunset = response_weather.json()["results"]["sunset"]
time_now = datetime.now().hour
night = int(sunset.split('T')[1].split(':')[0])  # past this hour
# iss_long = int(response_iss.json()["longitude"])
# iss_lat = int(response_iss.json()["latitude"])  # if within this lat and long
print(response_weather.json())
long_test = -70
la_test = 42
#  ejkf xnae vnwe igxy

password = "ejkf xnae vnwe igxy"
login_email = "szymonbryniakproject@gmail.com"

def check_iss(iss_lo, iss_la):

    while True:
        if time_now >= night:
            print('night')
        else:
            if MY_LONG - 5 <= iss_lo <= MY_LONG + 5 and MY_LAT - 5 <= la_test <= MY_LAT + 5:
                print('Go and watch iss')
                send_email()
            print('day')
        time.sleep(60)


def send_email():
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(password=password, user=login_email)
        connection.sendmail(msg="Go and watch iss", to_addrs="oneplusszymonbryniak@gmail.com", from_addr=login_email)
        connection.close()


check_iss(long_test, la_test)



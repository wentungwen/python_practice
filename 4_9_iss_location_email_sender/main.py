import time
import requests
import smtplib
import datetime as dt

my_email = "wen.for.programming@gmail.com"
password = "nggfhmsfqyqiairj"

MY_LAT = 36.7201600
MY_LNG = -4.4203400
TIME_UPDATE = 2

params = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0
}


def is_nighttime():
    res = requests.get("https://api.sunrise-sunset.org/json", params=params)
    res.raise_for_status()
    data = res.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    now_time = dt.datetime.now().hour
    if now_time < sunrise or now_time > sunset:
        return True


def is_overhead():
    iss_response = requests.get("http://api.open-notify.org/iss-now.json")
    iss_data = iss_response.json()["iss_position"]
    iss_lat = float(iss_data["latitude"])
    iss_lng = float(iss_data["longitude"])
    print(iss_lat, iss_lng)
    if MY_LAT - 5 <= iss_lat <= MY_LAT + 5 and MY_LNG - 5 <= iss_lng <= MY_LNG + 5:
        return True


def send_mail():
    with smtplib.SMTP("smtp.gmail.com", 587) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(from_addr=my_email, to_addrs="wentungwen@gmail.com",
                            msg=f"Subject: The current location of International "
                                f"Space Station\n\nLook up!")


while True:
    time.sleep(TIME_UPDATE)
    if not is_nighttime() and is_overhead():
        send_mail()
        print(123)

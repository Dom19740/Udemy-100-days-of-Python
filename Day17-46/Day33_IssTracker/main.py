import requests
import smtplib
import time
from datetime import datetime

MY_LAT = 38.736946  # Your latitude
MY_LONG = -9.142685  # Your longitude
MY_EMAIL = "tarsw002@gmail.com"
PASSWORD = "wjrvfuybeyywrgvl"


# function to return true if location is within +5 or -5 degrees of the ISS position.
def is_overhead():
    response = requests.get(url="http://api.open-notify.org/iss-now.json")
    response.raise_for_status()
    data = response.json()

    iss_latitude = float(data["iss_position"]["latitude"])
    iss_longitude = float(data["iss_position"]["longitude"])

    # iss_latitude = 33.8  # TEST DATA
    # iss_longitude = -5  # TEST DATA

    # print(iss_latitude)
    # print(iss_longitude)

    if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
        print("Is overhead")
        return True


# function to return true if its night
def is_night():

    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

    # print(sunrise)
    # print(sunset)

    hour_now = datetime.now().hour
    # hour_now = 20  # TEST DATA

    # print(hour_now)

    if hour_now < sunrise or sunset < hour_now:
        print("Is night")
        return True


def send_email():

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="dbuzugbe@gmail.com",
            msg=f"Subject: ISS\n\nLook Up"
        )
    # print("Email sent")


while True:
    time.sleep(5)

    if is_overhead() and is_night():
        send_email()
    # break  # TEST BREAK


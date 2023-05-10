import requests
from datetime import datetime

# # ISS request
# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
#
# data = response.json()
# print(data)
#
# longitude = data["iss_position"]["longitude"]
# latitude = data["iss_position"]["latitude"]
#
# iss_position = (longitude, latitude)
#
# print(iss_position)



# Sunrise sunset request
MY_LAT = 38.736946
MY_LNG = -9.142685

# set parameters to ask for lisbon
parameters = {
    "lat": MY_LAT,
    "lng": MY_LNG,
    "formatted": 0,  # get in 24hr format
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
# print(data)

# get data and split strings to get only hour values
sunrise = data["results"]["sunrise"].split("T")[1].split(":")[0]
sunset = data["results"]["sunset"].split("T")[1].split(":")[0]

print(sunrise)
print(sunset)

time_now = datetime.now()

print(time_now.hour)
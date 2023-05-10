import requests
from datetime import datetime, timedelta
from geopy.geocoders import Nominatim
from twilio.rest import Client

url = "https://api.openweathermap.org/data/2.5/forecast"
twilio_account_sid = "ACa3c015cc5e6c0bfd001db9f617d88b1b"
twilio_auth_token = "xxx"

parameters = {
    "lat": 38.6992,
    "lon": -9.2204,
    "appid": "xxx",
}


def get_country_name(city, country):
    geolocator = Nominatim(user_agent='my-custom-user-agent')
    location = geolocator.geocode(f"{city}, {country}")
    return location.address.split(',')[-1].strip()


send_alert = False
response = requests.get(url, params=parameters)

# check if request was successful
if response.status_code == 200:
    # parse JSON data from API response
    data = response.json()

    # get location
    city_name = data['city']['name']
    country_code = data['city']['country']
    country_name = get_country_name(city_name, country_code)
    location = f"{city_name}, {country_name}"

# SUNNY ALERT
    forecasts = data["list"]
    now = datetime.now()
    next_12_hours = now + timedelta(hours=12)
    is_hot_and_sunny = False

    for forecast in forecasts:
        forecast_time = datetime.fromtimestamp(forecast["dt"])
        if forecast_time > next_12_hours:
            break
        weather = forecast["weather"][0]["description"]
        temp = forecast["main"]["temp"]
        is_sunny = "clear sky" in weather.lower() or "few clouds" in weather.lower()
        is_hot = temp > 22

    if is_sunny and is_hot:
        print(f"It's hot and sunny today in {location}! Where a hat 😎.")
        send_alert = True
    elif is_sunny:
        print(f"It's sunny but not very hot in {location}.")
    elif is_hot:
        print(f"It's hot but not very sunny in {location}.")
    else:
        print(f"It's not very hot or sunny in {location}.")



# RAIN ALERT
#     # get list of forecasted weather data for the next 24 hours
#     forecast_data = [forecast for forecast in data['list']
#                      if datetime.strptime(forecast['dt_txt'], '%Y-%m-%d %H:%M:%S')
#                      <= datetime.now() + timedelta(days=1)]
#
#     # check if any forecasted weather has an ID less than 700
#     forecast_alert = any(forecast['weather'][0]['id'] < 700 for forecast in forecast_data)
#
#     if forecast_alert:
#         print(f"\nThere is rain forecasted in {location} in the next 24 hours ☔.")
#         send_alert = True
#     else:
#         print(f"\nNo forecast alert in {location} in the next 24 hours 😎.")
# else:
#     print("\nError: API request was not successful.")


if send_alert:

    client = Client(twilio_account_sid, twilio_auth_token)

    # #  send sms
    # message = client.messages \
    #     .create(
    #     body=f"There is rain forecasted in {location} in the next 24 hours ☔.",
    #     from_='+12708125618',
    #     to='+34652678183'
    # )

    # send whatsapp
    message = client.messages.create(
        from_='whatsapp:+14155238886',
        body=f"Weather Alert!\nHey Dom,\nIt´s hot and sunny in {location} today. Where a hat 😎!",
        to='whatsapp:+34652678183'
    )
    print(message.status)

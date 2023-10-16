import requests
import os
from datetime import datetime

#environment keys added to 'Edit Configuration´in Pycharm
APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
SHEET_ENDPOINT = os.environ["SHEET_ENDPOINT"]
TOKEN = os.environ["TOKEN"]

GENDER = "male"
WEIGHT_KG = 80
HEIGHT_CM = 190
AGE = 48

exercise_text = input("Tell me which exercises you did: ")

# Use nutrition x to convert typed string into usable json
nutritionix_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

nutritionix_headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

nutritionix_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(url=nutritionix_endpoint, json=nutritionix_params, headers=nutritionix_headers)
# print(response.text)

nutritionix_data = response.json()

# get the data and send to the sheet
today = datetime.now()

for entry in nutritionix_data['exercises']:
    sheety_params = {
        'workout': {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%H:%M:%S"),
            "exercise": entry['name'],
            "duration": entry['duration_min'],
            "calories": entry['nf_calories']
        }
    }

    print(f"\nExercise: {entry['name']}")
    print(f"Minutes: {entry['duration_min']}")
    print(f"Calories: {entry['nf_calories']}")

    headers = {'Authorization': TOKEN}

    response = requests.post(SHEET_ENDPOINT, json=sheety_params, headers=headers)

    if response.ok:
        sheety_data = response.json()
    else:
        print('Error:', response.status_code, response.text)



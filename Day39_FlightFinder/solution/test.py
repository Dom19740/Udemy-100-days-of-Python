import requests
from flight_data import FlightData

TEQUILA_ENDPOINT = "https://tequila-api.kiwi.com"
TEQUILA_API_KEY = 'PVDAadeyx3lz4W4enwiDfFFMXbsI6FY1'


location_endpoint = f"{TEQUILA_ENDPOINT}/locations/query"
headers = {"apikey": TEQUILA_API_KEY}
query = {
    "term": "London",
    "location_types": "city"
}
response = requests.get(url=location_endpoint, headers=headers, params=query)
results = response.json()["locations"]
code = results[0]["code"]
print(code)


headers = {"apikey": TEQUILA_API_KEY}
query = {
    "fly_from": "LON",
    "fly_to": "JFK",
    "date_from": "01/08/2023",
    "date_to": "01/09/2023",
    "nights_in_dst_from": 7,
    "nights_in_dst_to": 28,
    "flight_type": "round",
    "one_for_city": 1,
    "max_stopovers": 0,
    "curr": "GBP"
}

response = requests.get(
    url=f"{TEQUILA_ENDPOINT}/v2/search",
    headers=headers,
    params=query,
)

data = response.json()
print(data)

# try:
#     data = response.json()["data"][0]
# except IndexError:
#     print(f"No flights found for {destination_city_code}.")
#     return None


"""
flight_data = FlightData(
    price=data["price"],
    origin_city=data["route"][0]["cityFrom"],
    origin_airport=data["route"][0]["flyFrom"],
    destination_city=data["route"][0]["cityTo"],
    destination_airport=data["route"][0]["flyTo"],
    out_date=data["route"][0]["local_departure"].split("T")[0],
    return_date=data["route"][1]["local_departure"].split("T")[0]
)
print(f"{flight_data.destination_city}: £{flight_data.price}")
return flight_data
"""
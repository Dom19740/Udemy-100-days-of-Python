import requests
from datetime import datetime

USERNAME = "sydzxzhtwww"
TOKEN = "ads73523nfbs832nffdsf29"
GRAPH_ID = "graph1"

pixela_endpoint = "https://pixe.la/v1/users"

# pass token as a header for security
headers = {
    "X-USER-TOKEN": TOKEN
}

"""CREATE A USER"""
# user_params = {
#     "token": TOKEN,  # made up by me
#     "username": USERNAME,  # made up by me
#     "agreeTermsOfService": "yes",
#     "notMinor": "yes",
# }
##
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)


"""CREATE A GRAPH"""
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
#
# graph_config = {
#     "id": "graph1",
#     "name": "Coding Study Graph",
#     "unit": "Hrs",
#     "type": "float",
#     "color": "ichou"
# }
#
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)


"""CREATE A PIXEL"""
pixel_create_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

pixel_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today? "),
}

response = requests.post(url=pixel_create_endpoint, json=pixel_config, headers=headers)
print(response.text)


"""UPDATE A PIXEL"""
# pixel_update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230511"
#
# pixel_update_config = {
#     "quantity": "3.5",
# }
#
# response = requests.put(url=pixel_update_endpoint, json=pixel_update_config, headers=headers)
# print(response.text)


"""DELETE A PIXEL"""
# pixel_delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/20230511"
#
# response = requests.delete(url=pixel_delete_endpoint, headers=headers)
# print(response.text)
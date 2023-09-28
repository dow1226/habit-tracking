import requests
from datetime import datetime
from settings import PIXELA_APIKEY, PIXELA_USERNAME

pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": PIXELA_APIKEY,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes",
}
# response = requests.post(url=pixela_endpoint, json=user_params)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs"

graph_config = {
    "id": "graph1",
    "name": "drug Graph",
    "unit": "pieces",
    "type": "float",
    "color": "kuro",
}

headers = {
    "X-USER-TOKEN": PIXELA_APIKEY,
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

pixel_creation_endpoint = f"{pixela_endpoint}/{PIXELA_USERNAME}/graphs/graph1"
today = datetime.now()

pixel_data = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many drugs did you take today? "),
}

response = requests.post(url=pixel_creation_endpoint, json=pixel_data, headers=headers)
print(response.text)

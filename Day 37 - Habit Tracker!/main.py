import requests
from datetime import datetime

USERNAME = "felipecoimbra"
TOKEN = "harudaora130901"
GRAPHID = "graph1"

pixela_endpoint ="https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url= pixela_endpoint, json= user_params)
#print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_configuration = {
    "id": "graph1",
    "name": "Coding Graph",
    "unit": "hour",
    "type": "float",
    "color": "sora"
}

headers = {
    "X-USER-TOKEN": TOKEN,
}

#response = requests.post(url= graph_endpoint, json=graph_configuration, headers=headers)
#print(response.text)

paint_endpoint = f"{graph_endpoint}/{GRAPHID}"

today = datetime(year= 2022, month= 6, day= 21)
formated_today = today.strftime("%Y%m%d")

paint_configuration = {
    "date":formated_today,
    "quantity": "6",

}

#response = requests.post(url= paint_endpoint, json= paint_configuration, headers=headers)
#print(response.text)

update_pixel_endpoint = f"{paint_endpoint}/20220620"

update_config = {
    "quantity": "6",
}



#response = requests.put(url= update_pixel_endpoint, json= update_config, headers= headers)
responde = requests.delete(url=update_pixel_endpoint, headers= headers)

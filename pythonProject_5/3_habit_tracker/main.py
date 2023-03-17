import requests
import datetime as dt

# FINAL LINK: https://pixe.la/v1/users/wentungwen/graphs/graph1.html
USERNAME = "wentungwen"
TOKEN = "uo78irty"

pixela_endpoint = "https://pixe.la/v1/users"
post_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

## Send the request
# response = requests.post(url=pixela_endpoint, json=post_params)
# print(response.text)

## Create the graph
# https://pixe.la/v1/users/wentungwen/graphs/graph1.html
graph_config = {
    "id": "graph1",
    "name": "my cycling graph",
    "unit": "kilometer",
    "type": "float",
    "color": "sora"
}
headers = {
    "X-USER-TOKEN": TOKEN
}
# graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
# response = requests.post(url=graph_endpoint, json=graph_config, headers=headers)
# print(response.text)

NOW = dt.datetime.now().strftime("%Y%m%d")


## post a pixel
pixel_config = {
    "date": NOW,
    "quantity": input("How many distance today?")
}
pixel_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}"
response = requests.post(url=pixel_endpoint, json=pixel_config, headers=headers)
print(response.text)


## Put/update a pixel
update_config = {
    "quantity": "2"
}
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20230301"
# response = requests.put(url=update_endpoint, json=update_config, headers=headers)
# print(response.text)


## Delete a pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{graph_config['id']}/20230301"
# response = requests.delete(url=update_endpoint, headers=headers)
# print(response.text)

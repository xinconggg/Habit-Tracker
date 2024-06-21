import requests
import random

USERNAME = "xincong"
TOKEN = "jnad2nqionedjkand21noi3n1ja"
GRAPH_ID = "graph1"
pixela_endpoint = "https://pixe.la/v1/users"

## https://pixe.la/
# Create your user account (https://docs.pixe.la/entry/post-user)
user_params = {
    "token": TOKEN,  # Can be any string of length 8 - 128
    "username": USERNAME,  # Can be any string 
    "agreeTermsOfService": "yes", # Either "yes" or "no"
    "notMinor": "yes" # Either "yes" or "no"
}
response = requests.post(url=pixela_endpoint, json=user_params)

# Create a graph definition (https://docs.pixe.la/entry/post-graph)
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"
request_headers = {
    "X-USER-TOKEN": TOKEN
}
graph_params = {
    "id": GRAPH_ID,
    "name": "Running Graph",
    "unit": "Km",
    "type": "float",
    "color": "ajisai"
}
response = requests.post(url=graph_endpoint, json=graph_params, headers=request_headers)

# Plot value to the graph (https://docs.pixe.la/entry/post-pixel)
value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
value_params = {
    "date": "20240622",
    "quantity": "6.92"
}
response = requests.post(url=value_endpoint, json=value_params, headers=request_headers)
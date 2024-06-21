# [Pixe.la Graph Integration Habit Tracker](https://pixe.la/v1/users/xincong/graphs/graph1.html)
This project demonstrates how to use the Pixe.la API to create a user account, define a graph, and log values to track activities. The example focuses on tracking running distances.
![Screenshot 2024-06-21 111706](https://github.com/xinconggg/Habit-Tracker/assets/82378681/5247f492-ee99-46d3-91d6-1e08a722e3ca)

## Features
- Creates a user account on Pixe.la.
- Defines a graph for tracking activities.
- Logs data points to the created graph.

# Requirements
- Python 3.x
- requests library
- Pixe.la API token
## Installation
#### 1. Clone the repository:
```
git clone https://github.com/xinconggg/Habit-Tracker.git
cd pixela-graph-integration
```
#### 2. Install the required Python library:
```
pip install requests
```
#### 3. Set up environment variables for your Pixe.la API token and username. You can add these to a .env file or set them directly in your environment:
```
PIXELA_USERNAME=your_username
PIXELA_TOKEN=your_token
```

## Code Explanation
#### Creating a User Account
The script creates a user account on Pixe.la using the `requests` library:
```
import requests

USERNAME = "your_username"
TOKEN = "your_token"
pixela_endpoint = "https://pixe.la/v1/users"

user_params = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

response = requests.post(url=pixela_endpoint, json=user_params)
```
#### Creating a Graph
The script defines a graph for tracking activities:
```
GRAPH_ID = "graph1"
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
```
#### Logging a Value
The script logs a value to the defined graph:
```
value_endpoint = f"{graph_endpoint}/{GRAPH_ID}"
value_params = {
    "date": "20240622",  # YYYYMMDD format
    "quantity": "6.92"
}

response = requests.post(url=value_endpoint, json=value_params, headers=request_headers)
print(response.text)
```
For more detailed information on the Pixe.la API, please refer to the official [Pixe.la documentation](https://docs.pixe.la/).





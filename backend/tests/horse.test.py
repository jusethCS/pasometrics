import os
import requests
from dotenv import load_dotenv

# Load enviromental variables
load_dotenv()
token = os.getenv("TOKEN")

# API URL
url = 'http://ec2-54-88-30-239.compute-1.amazonaws.com/api/horse/'

# GET test: Query to database
response = requests.get(url, headers={'auth': token})
response.text

# POST test: Insert into database
data = {
    "id": "ASD 364863 -C GD",
    "name": "BARAJAS TOCATA DE AGUA BONITA",
    "birthday": "2022-05-28",
    "gender": "HEMBRA",
    "gait": "TROCHA",
}
response = requests.post(url, data=data, headers={'auth': token})
response.text
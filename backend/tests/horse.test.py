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
data = {"name": "PURA SANGRE"}
response = requests.post(url, data=data, headers={'auth': token})
response.text
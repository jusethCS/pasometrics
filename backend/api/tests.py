import os
import requests
from dotenv import load_dotenv

# API URL
url = 'http://ec2-54-88-30-239.compute-1.amazonaws.com/upload/'

# Setting the file and data
csv_file = {
    'MT': open('MT.csv', 'rb'),
    'M8': open('M8.csv', 'rb'),
    'DDT': open('DDT.csv', 'rb'),
    'DIT': open('DIT.csv', 'rb'),
    'PDT': open('PDT.csv', 'rb'),
    'PIT': open('PIT.csv', 'rb'),
    'DD8': open('DD8.csv', 'rb'),
    'DI8': open('DI8.csv', 'rb'),
    'PD8': open('PD8.csv', 'rb'),
    'PI8': open('PI8.csv', 'rb'),
}
#data = {'clave': 'valor'}

# Load enviromental variables
load_dotenv()
token = os.getenv("TOKEN")

# Send POST request
response = requests.post(url, files=csv_file, headers={'auth': token})#, data=data)

# Process the response
if response.status_code == 200:
    print("CSV file sent successfully")
else:
    print("Error sending CSV file:", response.text)


import os
import requests
from dotenv import load_dotenv

# API URL
url = 'http://ec2-54-88-30-239.compute-1.amazonaws.com/api/upload/'


# Setting the file and data
csv_file = {
    'MT': open('csv/MT.csv', 'rb'),
    'M8': open('csv/M8.csv', 'rb'),
    'DDT': open('csv/DDT.csv', 'rb'),
    'DIT': open('csv/DIT.csv', 'rb'),
    'PDT': open('csv/PDT.csv', 'rb'),
    'PIT': open('csv/PIT.csv', 'rb'),
    'DD8': open('csv/DD8.csv', 'rb'),
    'DI8': open('csv/DI8.csv', 'rb'),
    'PD8': open('csv/PD8.csv', 'rb'),
    'PI8': open('csv/PI8.csv', 'rb'),
}
data = {"test": "1"}

# Load enviromental variables
load_dotenv()
token = os.getenv("TOKEN")

# Send POST request
response = requests.post(url, files=csv_file, headers={'auth': token}, data=data)

# Process the response
if response.status_code == 200:
    print("CSV file sent successfully")
else:
    print("Error sending CSV file:", response.text)


import os
import requests
from dotenv import load_dotenv

# API URL
url = 'http://ec2-54-88-30-239.compute-1.amazonaws.com/api/upload/'


# Setting the file and data
csv_file = {'file': open('csv/MT.csv', 'rb')}
data = {"test": "1", "table": "M"}

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


# To download CSV data
# http://ec2-54-88-30-239.compute-1.amazonaws.com/api/csv?table=MT
import requests

# API URL
url = 'http://ec2-54-88-30-239.compute-1.amazonaws.com/upload/'

# Setting the file and data
csv_file = {
    'MT': open('MT.csv', 'rb')
}
#data = {'clave': 'valor'}

# Send POST request
response = requests.post(url, files=csv_file)#, data=data)

# Process the response
if response.status_code == 200:
    print("CSV file sent successfully")
else:
    print("Error sending CSV file:", response.text)

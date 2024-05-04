import csv
import pandas as pd

def get_data(request, filename):
    """
    Function to read and parse a CSV file uploaded via a request object.

    Args:
        - request: The HTTP request object containing the uploaded file.
        - filename: The name of the file uploaded.

    Returns:
        - DataFrame: A Pandas DataFrame containing the data from the CSV file.
    """
    # Access the uploaded CSV file from the request object
    csv_file = request.FILES[filename]
    
    # Read the CSV content and parse to dataframe
    decoded_file = csv_file.read().decode('utf-8')
    reader = csv.reader(decoded_file.splitlines())
    df = pd.DataFrame(reader, columns=next(reader))
    
    # Return the DataFrame containing the CSV data
    return df


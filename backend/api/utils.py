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
    df = df.drop(columns=['Index'])

    # Rename colunms
    table = filename.lower()
    df = df.rename(columns={
        "Date":"date",
        "Time":"time",
        "Recording Time":"recording_time",
        "Heart Rate":f"heart_rate_{table}",
        "Step Count":f"step_count_{table}",
        "Acceleration - X":f"ax_{table}",
        "Acceleration - Y":f"ay_{table}",
        "Acceleration - Z":f"az_{table}",
        "Attitude - Pitch":f"pitch_{table}",
        "Attitude - Roll":f"roll_{table}",
        "Attitude - Yaw":f"yaw_{table}",
        "Rotation - X":f"rx_{table}",
        "Rotation - Y":f"ry_{table}",
        "Rotation - Z":f"rz_{table}",
        "Gravity - X":f"gx_{table}",
        "Gravity - Y":f"gy_{table}",
        "Gravity - Z":f"gz_{table}"
    })
    
    # Return the DataFrame containing the CSV data
    return df


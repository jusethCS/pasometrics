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

    # Rename colunms
    df = df.rename(columns={
        "Index":"index",
        "Date":"date",
        "Time":"time",
        "Recording Time":"recording_time",
        "Heart Rate":"heart_rate",
        "Step Count":"step_count",
        "Acceleration - X":"ax",
        "Acceleration - Y":"ay",
        "Acceleration - Z":"az",
        "Attitude - Pitch":"pitch",
        "Attitude - Roll":"roll",
        "Attitude - Yaw":"yaw",
        "Rotation - X":"rx",
        "Rotation - Y":"ry",
        "Rotation - Z":"rz",
        "Gravity - X":"gx",
        "Gravity - Y":"gy",
        "Gravity - Z":"gz"
    })
    
    # Return the DataFrame containing the CSV data
    return df


import csv
import psycopg2
import pandas as pd
from sqlalchemy import create_engine

def get_data(request, filename, token):
    """
    Function to read and parse a CSV file uploaded via a request object.

    Args:
        - request: The HTTP request object containing the uploaded file.
        - filename: The name of the file uploaded.
        - token: Token for DB connection

    Returns:
        - DataFrame: A Pandas DataFrame containing the data from the CSV file.
    """
    # Access the uploaded CSV file from the request object
    csv_file = request.FILES[filename]
    
    # Read the CSV content and parse to dataframe
    decoded_file = csv_file.read().decode('utf-8')
    reader = csv.reader(decoded_file.splitlines())
    df = pd.DataFrame(reader, columns=next(reader))

    # Add test ID
    df['_test_id'] = request.POST.get("test")

    # Rename colunms
    df = df.rename(columns={
        "Index":"index",
        "Date":"date",
        "Time":"time",
        "Recording Time":"recording_time",
        "Heart Rate":"heart_rate",
        "Step Count":"step_count",
        "Acceleration - X":"acceleration_x",
        "Acceleration - Y":"acceleration_y",
        "Acceleration - Z":"acceleration_z",
        "Attitude - Pitch":"attitude_pitch",
        "Attitude - Roll":"attitude_roll",
        "Attitude - Yaw":"attitude_yaw",
        "Rotation - X":"rotation_x",
        "Rotation - Y":"rotation_y",
        "Rotation - Z":"rotation_z",
        "Gravity - X":"gravity_x",
        "Gravity - Y":"gravity_y",
        "Gravity - Z":"gravity_z"
    })

    # Insert data into DB
    table = filename.lower()
    db = create_engine(token)
    con = db.connect()
    df.to_sql(table, con=con, if_exists='append', index=False)
    con.close()
    
    # Return the DataFrame containing the CSV data
    return df


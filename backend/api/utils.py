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
        "Index":"_index",
        "Date":"_date",
        "Time":"_time",
        "Recording Time":"_recording_time",
        "Heart Rate":"_heart_rate",
        "Step Count":"_step_count",
        "Acceleration - X":"_acceleration_x",
        "Acceleration - Y":"_acceleration_y",
        "Acceleration - Z":"_acceleration_z",
        "Attitude - Pitch":"_attitude_pitch",
        "Attitude - Roll":"_attitude_roll",
        "Attitude - Yaw":"_attitude_yaw",
        "Rotation - X":"_rotation_x",
        "Rotation - Y":"_rotation_y",
        "Rotation - Z":"_rotation_z",
        "Gravity - X":"_gravity_x",
        "Gravity - Y":"_gravity_y",
        "Gravity - Z":"_gravity_z"
    })

    # Insert data into DB
    table = filename.lower()
    db = create_engine(token)
    con = db.connect()
    df.to_sql(table, con=con, if_exists='append', index=False)
    con.close()
    
    # Return the DataFrame containing the CSV data
    return df


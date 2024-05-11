###############################################################################
#                         LIBRARIES AND DEPENDENCIES                          #
###############################################################################
import os
import jwt
import csv
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt



###############################################################################
#               ENVIRONMENTAL VARIABLES AND TOKEN CONNECTIONS                 #
###############################################################################
# Enviromental variables
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")

# Generate the conection token
token = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}"



###############################################################################
#                       UTILS AND AUXILIAR FUNCTIONS                          #
###############################################################################
def insert_data(request):
    """
    Function to insert a CSV file into DB via a request object.

    Args:
        - request: The HTTP request object containing the uploaded file.
    """
    # Access the uploaded CSV file from the request object
    csv_file = request.FILES["file"]
    
    # Read the CSV content and parse to dataframe
    decoded_file = csv_file.read().decode('utf-8')
    reader = csv.reader(decoded_file.splitlines())
    df = pd.DataFrame(reader, columns=next(reader))

    # Add test ID
    df['test_id'] = request.POST.get("test")

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
    table = request.POST.get("table").lower()
    db = create_engine(token)
    con = db.connect()
    df.to_sql(table, con=con, if_exists='append', index=False)
    con.close()



###############################################################################
#                               MAIN CONTROLLER                               #
###############################################################################
@csrf_exempt
def data_controller(request):
    # Verify the token
    auth_token = request.headers.get('auth')
    if not auth_token:
        response = {'error': 'Token no provided'}
        return JsonResponse(response, status=401)
    try:
        jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
    except jwt.ExpiredSignatureError:
        response = {'error': 'Expired token'}
        return JsonResponse(response, status=401)
    except jwt.InvalidTokenError:
        response = {'error': 'Invalid token'}
        return JsonResponse(response, status=401)
    
    # POST token
    if request.method == 'POST':
        # Determine the test is provided
        test_id = request.POST.get('test', None)
        if test_id is None:
            return JsonResponse({'error': 'Field "test" is required'}, status=400)
        
        # Determine the table is provided
        table_id = request.POST.get('table', None)
        if table_id is None:
            return JsonResponse({'error': 'Field "table" is required'}, status=400)

        # Read and format data
        insert_data(request)

        response = {'message': 'CSV file processed successfully'}
        return JsonResponse(response)
    else:
        response = {'error': 'Expected a POST request with attached files'}
        return JsonResponse(response, status=400)



def view_csv_data(request):
    # Define table to query
    table = request.GET.get('table')

    # Query to database                     
    db = create_engine(token)
    con = db.connect()
    data = pd.read_sql(f"select * from {table.lower()};", con)
    con.close()

    # Convertir el DataFrame en un archivo CSV
    csv_data = data.to_csv(index=False)

    # Crear una respuesta HTTP con el archivo CSV como contenido
    response = HttpResponse(csv_data, content_type='text/csv')
    response['Content-Disposition'] = f'attachment; filename="{table}.csv"'
    return response







# http://ec2-54-88-30-239.compute-1.amazonaws.com/get-data?table=MT

#Nombre de los archivos:
#CSV del lugar donde se ubican los sensors en el caballo. 

# MT = Montador en la tabla (cuando el caballo va en linea recta)
# M8 = Montador en 8 (cuando el caballo va circulos hacienda el “8”)
# DDT = pata Delantero derecho en la tabla
# DIT = pata Delantero Izquierdo en la tabla
# PDT = pata Posterior derecho en la tabla
# PIT = pata Posterior Izquierdo en la tabla
# DD8 = pata delantero derecho en el 8
# DI8 = pata delantera izquierda en el 8
# PD8 = pata posterior derecho en el 8
# PI8 = posterior izquierda en el 8

import os
import jwt
import psycopg2
import pandas as pd
from .utils import get_data
from sqlalchemy import create_engine
from django.http import JsonResponse, HttpResponse
from django.views.decorators.csrf import csrf_exempt


# Enviromental variables
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")


# Generate the conection token
token = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}"


@csrf_exempt
def process_csv_file(request):
    if request.method == 'POST':
        # Verify the token was provided
        auth_token = request.headers.get('auth')
        if not auth_token:
            return JsonResponse({'error': 'Auth token was not provided'}, status=401)
        try:
            jwt.decode(auth_token, SECRET_KEY, algorithms=['HS256'])
        except jwt.ExpiredSignatureError:
            return JsonResponse({'error': 'Expired token'}, status=401)
        except jwt.InvalidTokenError:
            return JsonResponse({'error': 'Invalid token'}, status=401)

        # Read and format data
        MT = get_data(request=request, filename="MT", token=token)
        M8 = get_data(request=request, filename="M8", token=token)
        DDT = get_data(request=request, filename="DDT", token=token)
        DIT = get_data(request=request, filename="DIT", token=token)
        PDT = get_data(request=request, filename="PDT", token=token)
        PIT = get_data(request=request, filename="PIT", token=token)
        DD8 = get_data(request=request, filename="DD8", token=token)
        DI8 = get_data(request=request, filename="DI8", token=token)
        PD8 = get_data(request=request, filename="PD8", token=token)
        PI8 = get_data(request=request, filename="PI8", token=token)
        
        # Join dataframes
        dfs = [MT, M8, DDT, DIT, PDT, PIT, DD8, DI8, PD8, PI8]

        #print(MT)
        return JsonResponse({'message': 'CSV file processed successfully'})
    else:
        json = {'error': 'Expected a POST request with attached files'}
        return JsonResponse(json, status=400)



def view_csv_data(request):
    table = request.GET.get('table')
                            
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

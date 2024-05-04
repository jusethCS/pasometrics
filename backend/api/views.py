import os
import psycopg2
from .utils import get_data
from sqlalchemy import create_engine
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt


# Enviromental variables
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv('DB_NAME')

# Generate the conection token
token = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}"


@csrf_exempt
def process_csv_file(request):
    if request.method == 'POST':
        MT = get_data(request=request, filename="MT")
        # test
        db = create_engine(token)
        con = db.connect()
        MT.to_sql("prueba", con=con, if_exists='replace', index=True)
        con.close()
        #print(MT)
        return JsonResponse({'message': 'CSV file processed successfully'})
    else:
        json = {'error': 'Expected a POST request with attached files'}
        return JsonResponse(json, status=400)








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

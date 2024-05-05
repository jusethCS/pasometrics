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
def horse_crud(request):
    if request.method == 'GET': 
        # Query to database                  
        db = create_engine(token)
        con = db.connect()
        data = pd.read_sql(f"select * from horse;", con)
        con.close()

        # Response
        return JsonResponse(data.to_json(orient='records'), safe=False)
    
    if request.method == 'POST':
        # Retrieve horse name
        name = request.POST.get('name', None)
        if name is None:
            return JsonResponse({'error': 'El campo "name" es requerido'}, status=400)

        # Insert into database
        db = create_engine(token)
        con = db.connect()
        con.execute(f"INSERT INTO horse (name) VALUES ('{name}');")
        data = pd.read_sql(f"select * from horse where name='{name}';", con)
        con.close()

        # Response: ID for inserted horse
        return JsonResponse(data.to_json(orient='records'), safe=False)

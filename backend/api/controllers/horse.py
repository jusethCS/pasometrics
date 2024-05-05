import os
import jwt
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from django.http import JsonResponse


# Enviromental variables
DB_USER = os.getenv("DB_USER")
DB_PASS = os.getenv("DB_PASS")
DB_NAME = os.getenv("DB_NAME")
SECRET_KEY = os.getenv("SECRET_KEY")


# Generate the conection token
token = f"postgresql+psycopg2://{DB_USER}:{DB_PASS}@localhost:5432/{DB_NAME}"


# Main Controller
def horse(request):
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
        
    if request.method == 'GET': 
        # Query to database                  
        db = create_engine(token)
        con = db.connect()
        data = pd.read_sql(f"select * from horse;", con)
        con.close()
    
    if request.method == 'POST':
        # Retrieve horse name
        name = request.POST.get('name', None)
        if name is None:
            return JsonResponse({'error': 'Field "name" is required'}, status=400)

        # Insert into database
        db = create_engine(token)
        con = db.connect()
        df = pd.DataFrame({'name': [name]})
        df.to_sql("horse", con=con, if_exists='append', index=False)
        data = pd.read_sql(f"select * from horse where name='{name}';", con)
        con.close()

    # Response
    return JsonResponse(data.to_dict(orient='records'), safe=False)

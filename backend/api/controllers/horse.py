###############################################################################
#                         LIBRARIES AND DEPENDENCIES                          #
###############################################################################
import os
import jwt
import psycopg2
import pandas as pd
from sqlalchemy import create_engine
from django.http import JsonResponse
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
#                               MAIN CONTROLLER                               #
###############################################################################
@csrf_exempt
def horse_controller(request):
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
        # Retrieve horse id
        idr = request.POST.get('id', None)
        if idr is None:
            return JsonResponse({'error': 'Field "id" is required'}, status=400)
        
        # Retrieve horse name
        name = request.POST.get('name', None)
        if name is None:
            return JsonResponse({'error': 'Field "name" is required'}, status=400)
        
        # Retrieve other horse properties
        birthday = request.POST.get('birthday')       
        gait = request.POST.get('gait').upper()
        gender = request.POST.get('gender').upper()
        
        # Insert into database
        db = create_engine(token)
        con = db.connect()
        df = pd.DataFrame({
            'id': [idr],
            'name': [name],
            'birthday': [birthday],
            'gender': [gender],
            'gait': [gait]})
        df.to_sql("horse", con=con, if_exists='append', index=False)
        data = pd.read_sql(f"select * from horse where id='{idr}';", con)
        con.close()

    # Response
    return JsonResponse(data.to_dict(orient='records'), safe=False)

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
def test_controller(request):
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
        data = pd.read_sql(f"select * from test;", con)
        con.close()
    
    if request.method == 'POST':
        #Retrieve horse id
        horse = request.POST.get('horse', None)
        if horse is None:
            return JsonResponse({'error': 'Field "horse" is required'}, status=400)
        
        #Retrieve datetime
        date = request.POST.get('datetime', None)
        if date is None:
            return JsonResponse({'error': 'Field "datetime" is required'}, status=400)
        
        #Retrieve test type
        testType = request.POST.get('testType', None)
        if testType is None:
            return JsonResponse({'error': 'Field "testType" is required'}, status=400)
        if not(testType in ["T", "8"]):
            return JsonResponse({'error': 'Field "testType" would be "T" or "8"'}, status=400)

        # Insert into database
        db = create_engine(token)
        con = db.connect()
        df = pd.DataFrame({'horse': [horse.upper()], 'date':[date], 'type': [testType]})
        df.to_sql("test", con=con, if_exists='append', index=False)
        data = pd.read_sql(f"select * from test where horse='{horse}' and date='{date}';", con)
        con.close()

    # Response
    return JsonResponse(data.to_dict(orient='records'), safe=False)
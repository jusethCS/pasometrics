
@csrf_exempt
def process_csv_file(request):
    if request.method == 'POST':
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
        
        # request.POST.get("horseId")
        # Read and format data
        MT = get_data(request,"MT", token)
        M8 = get_data(request,"M8", token)
        DDT = get_data(request,"DDT", token)
        DIT = get_data(request,"DIT", token)
        PDT = get_data(request,"PDT", token)
        PIT = get_data(request,"PIT", token)
        DD8 = get_data(request,"DD8", token)
        DI8 = get_data(request,"DI8", token)
        PD8 = get_data(request,"PD8", token)
        PI8 = get_data(request,"PI8", token)

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

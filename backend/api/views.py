import pandas as pd
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def procesar_archivo_csv(request):
    if request.method == 'POST' and request.FILES.get('archivo'):
        archivo_csv = request.FILES['archivo']
        try:
            decoded_file = archivo_csv.read().decode('utf-8')
            reader = csv.reader(decoded_file.splitlines())
            
            # Convertir el CSV a un DataFrame de pandas
            df = pd.DataFrame(reader, columns=next(reader))
            
            # Aquí puedes procesar el DataFrame según tus necesidades
            print(df)
            
            # Puedes devolver el DataFrame en formato JSON si es necesario
            return JsonResponse({'mensaje': 'Archivo CSV procesado correctamente', 'datos': df.to_json(orient='records')})
        except Exception as e:
            return JsonResponse({'error': 'Error al procesar el archivo CSV: {}'.format(str(e))}, status=400)
    else:
        return JsonResponse({'error': 'Se esperaba una solicitud POST con un archivo adjunto'}, status=400)

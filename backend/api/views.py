#from django.shortcuts import render
import csv
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@csrf_exempt
def procesar_archivo_csv(request):
    if request.method == 'POST' and request.FILES.get('archivo'):
        archivo_csv = request.FILES['archivo']
        # Lee el archivo CSV
        datos = []
        try:
            decoded_file = archivo_csv.read().decode('utf-8')
            reader = csv.reader(decoded_file.splitlines())
            for row in reader:
                datos.append(row)
            # Aquí puedes procesar los datos como desees
            print(datos)
            #
            return JsonResponse({'mensaje': 'Archivo CSV procesado correctamente', 'datos': datos})
        except Exception as e:
            return JsonResponse({'error': 'Error al procesar el archivo CSV: {}'.format(str(e))}, status=400)
    else:
        return JsonResponse({'error': 'Se esperaba una solicitud POST con un archivo adjunto'}, status=400)

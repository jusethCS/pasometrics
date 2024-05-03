from django.urls import path
from .views import procesar_archivo_csv

urlpatterns = [
    path('upload/', procesar_archivo_csv, name='procesar_csv'),
]
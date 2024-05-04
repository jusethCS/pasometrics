from django.urls import path
from .views import process_csv_file, view_csv_data

urlpatterns = [
    path('upload/', process_csv_file, name='process_csv_file'),
    path('get-data/', view_csv_data, name='view_csv_data'),
]
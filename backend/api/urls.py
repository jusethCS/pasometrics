from django.urls import path
from .views import process_csv_file

urlpatterns = [
    path('upload/', process_csv_file, name='process_csv_file'),
]
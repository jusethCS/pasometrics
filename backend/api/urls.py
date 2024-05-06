from django.urls import path
from .controllers.horse import horse_controller
from .controllers.horsetest import test_controller
from .controllers.data import data_controller, view_csv_data

urlpatterns = [
    path('horse/', horse_controller, name='horse'),
    path('test/', test_controller, name='test'),
    path('upload/', data_controller, name='data'),
    path('csv/', view_csv_data, name='view')
]
from django.urls import path
from .controllers.horse import horse_controller
from .controllers.horsetest import test_controller

urlpatterns = [
    path('horse/', horse_controller, name='horse'),
    path('test/', test_controller, name='test')
]
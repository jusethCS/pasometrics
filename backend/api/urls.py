from django.urls import path
from .controllers.horse import horse_controller

urlpatterns = [
    path('horse/', horse_controller, name='horse')
]
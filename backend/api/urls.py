from django.urls import path
from .views import horse_crud

urlpatterns = [
    path('horse/', horse_crud, name='horse')
]
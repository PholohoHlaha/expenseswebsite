from .views import Map
from django.urls import path
from  map.views import *


urlpatterns = [
    path('index', Map, name="index")
]
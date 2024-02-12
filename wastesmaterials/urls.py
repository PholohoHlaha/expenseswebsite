from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name="wastesmaterials"),
    path('add-wastes', views.add_wastes, name="add-wastes")

]
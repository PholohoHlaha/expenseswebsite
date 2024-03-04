from .views import Register,Login
from django.urls import path
from authentication.views import *

urlpatterns = [
    path('register', Register, name="register"),
    path('login', Login, name="login")
]
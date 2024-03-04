from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def Register(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        email = request.POST.get('email')
        plant_location = request.POST.get('plant_location')
        password = request.POST.get('password1')
        password2 = request.POST.get('password2')
        userType = request.POST.get('userType')

        new_user = User.objects.create_user(username, email, password)
        new_user.first_name = first_name
        new_user.last_name = last_name
        new_user.plant_location = plant_location
        new_user.password2 = password2
        new_user.userType = userType

        new_user.save()
        return redirect('login')
    return render(request, 'authentication/register.html', {})

def Login(request):
    if request.method == "POST":
        name = request.POST.get('uname')
        password = request.POST.get('pass')

        user = authenticate(request, username=name, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')  
        else:
            return HttpResponse('Error, user does not exist')

    return render(request, 'authentication/login.html')

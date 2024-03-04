from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request,'wastesmaterials/index.html')

def add_wastes(request):
    return render(request, 'wastesmaterials/add_wastes.html')
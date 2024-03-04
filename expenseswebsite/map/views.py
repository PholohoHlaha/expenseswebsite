from django.shortcuts import render
import folium 

# Create your views here.
def Map(request):
    return render(request, 'map/index.html')

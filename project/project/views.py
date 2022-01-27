from django.shortcuts import render
from rest_framework.decorators import api_view

# display the navigation bar at http://127.0.0.1:8000/
def display_home(request):  
    return render(request, 'home.html')
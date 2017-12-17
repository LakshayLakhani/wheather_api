import requests
import datetime

from django.shortcuts import render
from geopy.geocoders import Nominatim

def find_iss(request):

    response = requests.get("http://api.open-notify.org/iss-now.json")
    response_text =  response.text
    context = {}
    return render(request, "iss/find_iss.html", context)

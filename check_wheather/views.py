from django.shortcuts import render
from geopy.geocoders import Nominatim
import requests


def check_wheather(request):
    print "in check_wheather "
    zip = request.POST.get("zip_code")
    context = None
    if zip:
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+str(zip)+",IN&appid=9444619ff487bd8ce510df492ff72929")
        json_object = response.json()
        name = json_object['name']
        temperature_in_k = float(json_object['main']['temp'])
        temperature_in_C = (temperature_in_k - 273.15)
        print temperature_in_C
        context = {"temperature_in_C":temperature_in_C, "name":name}
    return render(request, "check_wheather/search_wheather.html", context)


# 9444619ff487bd8ce510df492ff72929 new


# 1c26171b74cf6867a48bede53e74521f old

def check_air_pollution(request):
    location = request.POST.get("location",)
    
    context = None
    if location:
        geolocator = Nominatim()
        location = geolocator.geocode(location)
        # print "location address +++++++++++++++++++++++"
        # print location.address
        # print "location latitude location longitude +++++++++++++++++++++++"

        print((location.latitude, location.longitude))
        response = requests.get("http://api.openweathermap.org/pollution/v1/co/"+location.latitude,location.longitude+"/{datetime}.json?appid=1c26171b74cf6867a48bede53e74521f")
        context = {"location":location,}
    return render(request,"check_wheather/check_air_pollution.html", context)

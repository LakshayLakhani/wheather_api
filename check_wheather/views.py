from django.shortcuts import render
import requests

def check_wheather(request):
    print "in check_wheather "
    zip = request.POST.get("zip_code")
    context = None
    if zip:
        print "in zip ++++++++++++++++"
        print zip
        response = requests.get("http://api.openweathermap.org/data/2.5/weather?zip="+str(zip)+",IN&appid=1c26171b74cf6867a48bede53e74521f")
        json_object = response.json()
        print json_object
        temperature =  float(json_object['main']['temp'])
        str_temperature = temperature
        print str_temperature
        context = {"str_temperature":str_temperature}
    return render(request, "check_wheather/search_wheather.html", context)

def wheather(request):
    print " in wheather "
    return render(request, "check_wheather/wheather.html", {})

import requests
import datetime
import json

from django.shortcuts import render
from geopy.geocoders import Nominatim, GoogleV3


def check_wheather(request):
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


def find_iss(request):
    response = requests.get("http://api.open-notify.org/iss-now.json")
    response_text =  response.text
    json_response = json.loads(response_text)
    latitude = json_response['iss_position']['latitude']
    longitude = json_response['iss_position']['longitude']

    context = {"iss_latitude":latitude, "iss_longitude":longitude,}

    return render(request, "check_wheather/find_iss.html", context)

def get_request(request):
    context = {}

    url = "http://maps.googleapis.com/maps/api/geocode/json"

    if request.method == "POST":
        location = request.POST.get("location")
        if location:
            PARAMS = {'address':location}
            r = requests.get(url = url, params = PARAMS)
            data = r.json()

            latitude = data['results'][0]['geometry']['location']['lat']
            longitude = data['results'][0]['geometry']['location']['lng']
            formatted_address = data['results'][0]['formatted_address']

            context.update({"latitude":latitude, "longitude":longitude, "formatted_address":formatted_address })
        else:
            pass



    return render(request, "check_wheather/get_request.html", context)

def post_request(request):
    context = {}
    url = "http://pastebin.com/api/api_post.php"
    api_key = "2605443e4d1603747167daa1c3c2a455"

    if request.method == "POST":
        source_code = request.POST.get("source_code",None)
        print source_code
        if source_code:
            data = {
                'api_dev_key':api_key,
                'api_option':'paste',
                'api_paste_code':source_code,
                'api_paste_format':'python'
            }
            response = requests.post(url=url, data=data)
            pastebin_url = response.text
            print "pastebin_url+++++++++++++++++++++++++++++++++++"
            print pastebin_url

            context.update({"pastebin_url":pastebin_url})
        else:
            pass

    return render(request, "check_wheather/post_request.html", context)

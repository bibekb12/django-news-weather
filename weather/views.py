import json
from django.shortcuts import render
import urllib.request
from django.conf import settings

from weather.models import Weather
from .serializers import weatherCreateSerializer, weatherListSerializer


def homepage(request):
    return render(request, "index.html")

def news(request):
    return render(request, "news.html") 

# Creating the view of weather
def weather_view(request):
    data = {}
    city =''
    if request.method == "POST":
        city = request.POST.get("city")
        try: 
            source = urllib.request.urlopen('http://api.openweathermap.org/data/2.5/weather?q=' + city + '&appid=' + settings.WEATHER_API_KEY + '&units=metric').read()
        except Exception as e:
            return render(request, "weather.html", {"status": e})
        
        list_of_data = json.loads(source)
        
        data = {
            "city": city,
            "country_code": str(list_of_data['sys']['country']),
            "temperature": str(list_of_data['main']['temp']),
            "pressure": str(list_of_data['main']['pressure']),
            "humidity": str(list_of_data['main']['humidity']),
            "description": str(list_of_data['weather'][0]['description']),
            "icon": str(list_of_data['weather'][0]['icon']),
            "status": "success",
        }
        serial = weatherCreateSerializer(data=data)
        if serial.is_valid():
            serial.save()
            return render(request, "weather.html", {"data": data,"city": city})
        else:
            return render(request, "weather.html", {"data": {"message": "Unexpected error"}})
        
    elif request.method == "GET":
        weather = Weather.objects.all()
        serial = weatherListSerializer(weather, many=True)
        return render(request, "weather.html", {"dataHistory": serial.data})
    
    else:
        return render(request, "weather.html", {"data": {}})
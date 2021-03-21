from django.shortcuts import render
from django.views import View
from .models import *
from .forms import *
import requests


def weather(request):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid=9e46f2e2eb2eb06ce112ba679387c082'

    if request.method == 'POST':
        form = CityForm(request.POST)
        form.save()
        
    form = CityForm()

    cities = City.objects.all()

    weather_data = []

    for city in cities:
        r = requests.get(url.format(city)).json()

        city_weather = {
            'city': city.name,
            'temperature': r['main']['temp'],
            'description': r['weather'][0]['description'],
            'icon': r['weather'][0]['icon'],
        }
        weather_data.append(city_weather)
    return render(request, 'weather/home.html', {'weather_data': weather_data, 'form': form})



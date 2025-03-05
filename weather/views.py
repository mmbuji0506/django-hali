from django.shortcuts import render, get_object_or_404
from .models import City, WeatherData
from .utils import get_weather_data
from django.conf import settings
import pytz
from datetime import datetime, timedelta

def home(request):
    cities = City.objects.all()
    weather_data = {}
    for city in cities:
        data = get_weather_data(city.name, settings.OPENWEATHERMAP_API_KEY)
        if data:
            data['id'] = city.id # added line
            weather_data[city.name] = data
    return render(request, 'weather/home.html', {'weather_data': weather_data})

def search_city(request):
    city_name = request.GET.get('city')
    if city_name:
        data = get_weather_data(city_name, settings.OPENWEATHERMAP_API_KEY)
        if data:
           timezone_offset = data.get('timezone') # get timezone, using .get to prevent keyerror
        if isinstance(timezone_offset, int): # checks if the value is an int
            offset_seconds = timedelta(seconds=timezone_offset)
            offset_hours = offset_seconds.total_seconds() / 3600
            if offset_hours == 0:
                timezone_str = 'Africa/Dar_es_Salaam'
            else:
                sign = '+' if offset_hours > 0 else '-'
                timezone_str = f'Etc/GMT{sign}{int(abs(offset_hours))}' # creates string in the format pytz understands
        elif isinstance(timezone_offset, str):
            timezone_str = timezone_offset # if it's already a string, keep it
        else:
            timezone_str = 'Africa/Dar_es_Salaam' # default to Africa/Dar_es_Salaam if no time zone info.

        city, created = City.objects.get_or_create(name=city_name, defaults={'timezone': pytz.timezone(timezone_str), 'latitude': data['coord']['lat'] if 'coord' in data else 0, 'longitude': data['coord']['lon'] if 'coord' in data else 0})
    WeatherData.objects.create(city=city, temperature=data['main']['temp'], humidity=data['main']['humidity'], description=data['weather'][0]['description'])
    return render(request, 'weather/search.html', {'weather_data': data, 'city': city})


def detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    weather_data = get_weather_data(city.name, settings.OPENWEATHERMAP_API_KEY)
    return render(request, 'weather/detail.html', {'weather_data': weather_data, 'city': city})
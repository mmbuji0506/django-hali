from django.shortcuts import render, get_object_or_404
from .models import City, WeatherData
from .utils import get_weather_data
from django.conf import settings
import logging, pytz
from datetime import datetime
from django.utils import timezone

logger = logging.getLogger(__name__)

def validate_pressure(pressure_value, city_name):
    if pressure_value is None:
        logger.error(f"Pressure is None for {city_name}")
        return 0.0
    elif isinstance(pressure_value, datetime):
        logger.error(f"Pressure is datetime for {city_name}: {pressure_value}")
        return 0.0
    else:
        try:
            return float(pressure_value)
        except (TypeError, ValueError) as e:
            logger.error(f"Pressure conversion failed for {city_name}: {pressure_value}, error: {e}")
            return 0.0

def home(request):
    cities = City.objects.all()
    weather_data = {}
    for city in cities:
        data = get_weather_data(city.name, settings.OPENWEATHERMAP_API_KEY)
        if data:
            data['id'] = city.id
            weather_data[city.name] = data
    return render(request, 'weather/home.html', {'weather_data': weather_data})

def search_city(request):
    context = {}
    city_name = request.GET.get('city')

    if city_name:
        data = get_weather_data(city_name, settings.OPENWEATHERMAP_API_KEY)
        print("Data from API:", data)
        if data is None:
            context['error'] = "Error retrieving weather data"
            return render(request, 'weather/search.html', context)
        if data:
            try:
                timezone_str = 'Africa/Dar_es_Salaam'
                timezone.activate(pytz.timezone(timezone_str))
                current_time = timezone.now()
                time_24hr = current_time.strftime('%H:%M:%S')
                city, created = City.objects.get_or_create(
                    name=city_name.title(),
                    defaults={
                        'timezone': pytz.timezone(timezone_str),
                        'latitude': data.get('coord', {}).get('lat', 0),
                        'longitude': data.get('coord', {}).get('lon', 0)
                    }
                )

                pressure = validate_pressure(data['main'].get('pressure'), city_name)
                print(f"Pressure (views.py, validated): {pressure}, Type: {type(pressure)}")

                weather_instance = WeatherData.objects.create(
                    city=city,
                    temperature=data['main']['temp'],
                    humidity=data['main']['humidity'],
                    pressure=pressure,
                    wind_speed=data['wind']['speed'],
                    description=data['weather'][0]['description'],
                    timestamp=current_time
                )

                context['weather_data'] = data
                context['city'] = city
                context['current_time'] = time_24hr

            except pytz.UnknownTimeZoneError:
                context['error'] = f"Invalid timezone for {city_name}"
            except KeyError as e:
                context['error'] = f"Missing data in API response: {str(e)}"
            except Exception as e:
                logger.exception("Error processing weather data:")
                context['error'] = "An unexpected error occurred."
        else:
            context['error'] = f"Weather data not found for {city_name}"
    else:
        context['error'] = "Please enter a city name"

    return render(request, 'weather/search.html', context)

def detail(request, city_id):
    city = get_object_or_404(City, pk=city_id)
    weather_data = get_weather_data(city.name, settings.OPENWEATHERMAP_API_KEY)
    return render(request, 'weather/detail.html', {'weather_data': weather_data, 'city': city})
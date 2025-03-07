import requests
from django.conf import settings

def get_weather_data(city_name, api_key):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': api_key,
        'units': 'metric'
    }
    try:
        response = requests.get(base_url, params=params)
        response.raise_for_status()
        data = response.json()
        print("Raw API Data:", data)
        return data
    except requests.exceptions.RequestException as e:
        print(f"Error fetching weather data: {e}")
        return None
    except ValueError as e:
        print(f"Error decoding JSON data: {e}")
        return None
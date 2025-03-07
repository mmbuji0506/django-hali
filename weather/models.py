from django.db import models
from django.utils import timezone
import pytz
from datetime import datetime

class City(models.Model):
    name = models.CharField(max_length=100, unique=True)
    timezone = models.CharField(max_length=50, default='UTC')
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.FloatField()
    pressure = models.FloatField(default=0.0)
    wind_speed = models.FloatField()
    description = models.CharField(max_length=255)
    timestamp = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.city.name} - {self.timestamp}"
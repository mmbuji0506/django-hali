from django.db import models
from timezone_field import TimeZoneField

class City(models.Model):
    name = models.CharField(max_length=100)
    timezone = TimeZoneField(default='UTC')
    latitude = models.FloatField(null=True, blank=True)
    longitude = models.FloatField(null=True, blank=True)

    def __str__(self):
        return self.name

class WeatherData(models.Model):
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    temperature = models.FloatField()
    humidity = models.IntegerField()
    description = models.CharField(max_length=200)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.city.name} - {self.timestamp}"
from django.db import models


class Weather(models.Model):
    city = models.CharField(max_length=100)
    country_code = models.CharField(max_length=10)
    temperature = models.CharField(max_length=10)
    pressure = models.CharField(max_length=10)
    humidity = models.CharField(max_length=10)
    description = models.CharField(max_length=100)
    icon = models.CharField(max_length=10)
    
    def __str__(self):
        return self.city
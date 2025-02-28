from django.urls import path, include
from .views import homepage, weather_view


urlpatterns = [
    path('', homepage, name="homepage"),
    path('weathers', weather_view, name="weather_view"),
    path('news',include('newsapp.urls'), name="news"),
]

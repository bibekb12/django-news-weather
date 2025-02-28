# import requests

# def get_weather_data(city):
#     API_KEY = "62ef74fc34ffce072c8acc8205ed6ecb"
#     url = "http://api.openweathermap.org/data/2.5/weather"
#     params = {"q": city, "appid":API_KEY, "units":"metric",}
#     response = requests.get(url, params=params)
#     return response.json()
from flask import request
from geopy.geocoders import Nominatim
from flask.views import MethodView
from weather.service import WeatherService


class WeatherResource(MethodView):

    def get(self):
        geolocator = Nominatim(user_agent="weather_api")
        lat = request.args.get('lat')
        lon = request.args.get('lon')
        weather_obj = WeatherService()
        weather_data = weather_obj.report(lat, lon)
        lat = weather_data['coord']['lat']
        lon = weather_data['coord']['lon']
        temp = int(weather_data['main']['temp'] - 273.15)
        humidity = int(weather_data['main']['humidity'])
        wind_speed = int(weather_data['wind']['speed'])
        location = geolocator.geocode(str(lat) + "," + str(lon))
        return {
            'temperature':  temp,
            'humidity': humidity,
            'wind_speed': wind_speed,
            'location': location.address
        }

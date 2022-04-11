import requests
from flask import current_app as app


class WeatherService:

    def __init__(self):
        self.api_key = app.config['API_KEY']
        self.report_url = f"https://api.openweathermap.org/data/2.5/weather?q=&appid={self.api_key}"

    def report(self, lat, lon):
        parameters = {
                "lat": lat,
                "lon": lon
        }
        response = requests.get(self.report_url, params=parameters)
        weather_data = response.json()
        return weather_data

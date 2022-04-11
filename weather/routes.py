from flask import Blueprint
from weather.controller import WeatherResource

weather = Blueprint('weather', __name__,  url_prefix='/weather')
weather.add_url_rule('/report', 'weather', WeatherResource.as_view('weather'))

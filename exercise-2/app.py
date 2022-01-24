import os
from unittest import result
import requests

from datetime import datetime, timedelta
from dotenv import load_dotenv
from flask import Flask, render_template, request, send_file
from geopy.geocoders import Nominatim


################################################
## SETUP
################################################

app = Flask(__name__)

load_dotenv()
API_KEY = os.getenv('API_KEY')


################################################
## ROUTES
################################################

@app.route('/')
def home():
    """Displays the homepage with forms for current or historical data."""
    context = {
        'min_date': (datetime.now() - timedelta(days=5)),
        'max_date': datetime.now()
    }
    return render_template('home.html', **context)

def get_letter_for_units(units):
    """Returns a shorthand letter for the given units."""
    return 'F' if units == 'imperial' else 'C' if units == 'metric' else 'K'

def get_lat_lon(city_name):
    geolocator = Nominatim(user_agent='Weather Application')
    location = geolocator.geocode(city_name)
    if location is not None:
        return location.latitude, location.longitude
    return 0, 0

@app.route('/results')
def results():
    """Displays results for current weather conditions."""
    city = request.args.get('users_city')
    units = request.args.get('requested_units')

    url = 'http://api.openweathermap.org/data/2.5/weather'

    latitude,longitude = get_lat_lon(city)
    params = {
        'appid': API_KEY,
        'lat' : latitude,
        'lon' : longitude,
        'units': units
    }
    result_json = requests.get(url, params=params).json()

    context = {
        'date': datetime.now(),
        'city': city,
        'description': result_json['weather'][0]['description'],
        'temp': result_json['main']['temp'],
        'humidity': result_json['main']['humidity'],
        'wind_speed': result_json['wind']['speed'],
        'units_letter': get_letter_for_units(units)
    }

    return render_template('results.html', **context)


if __name__ == '__main__':
    app.run()

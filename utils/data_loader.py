import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_URL = os.getenv("API_URL")


def load_data(city, days, hour):
    response = requests.get(API_URL, params={
        'key': API_KEY,
        'q': city,
        'days': days,
        'aqi': 'yes',
        'alerts': 'no'
    })
    data = response.json()

    city_name = data['location']['name']
    temp = data['current']['temp_c']
    condition = data['current']['condition']['text']
    icon = data['current']['condition']['icon']
    last_updated = data['current']['last_updated']

    forecast_days = data['forecast']['forecastday']
    days_labels = []
    co_vals = []
    no2_vals = []
    o3_vals = []
    so2_vals = []
    pm25_vals = []
    pm10_vals = []

    for day in forecast_days:
        days_labels.append(day['date'])
        hour_data = day['hour'][hour]
        air_quality = hour_data['air_quality']
        
        co_vals.append(air_quality['co'])
        no2_vals.append(air_quality['no2'])
        o3_vals.append(air_quality['o3'])
        so2_vals.append(air_quality['so2'])
        pm25_vals.append(air_quality['pm2_5'])
        pm10_vals.append(air_quality['pm10'])

    return {
        'city_name': city_name,
        'temp': temp,
        'condition': condition,
        'icon': icon,
        'last_updated': last_updated,
        'days_labels': days_labels,
        'co_avg': co_vals,
        'no2_avg': no2_vals,
        'o3_avg': o3_vals,
        'so2_avg': so2_vals,
        'pm25_avg': pm25_vals,
        'pm10_avg': pm10_vals
    }


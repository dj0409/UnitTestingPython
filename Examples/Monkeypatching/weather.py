import requests

def get_weather(city):
    response = requests.get(f"https://fake-weather.com/{city}")
    return response.json()
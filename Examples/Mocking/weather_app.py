def fetch_weather_data(api_client):
    response = api_client.get("https://api.weather.com/data")
    if response.status_code == 200:
        return response.json()
    else:
        return None
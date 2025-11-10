import requests


class WeatherForecastTool:

    def __init__(self, api_key: str):
        self.api_key = api_key
        self.base_url = "http://api.openweathermap.org/data/2.5/"

    def get_current_weather(self, city: str) -> dict:
        """Get the current weather for a city."""
        url = f"{self.base_url}weather?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return {}

    def get_weather_forecast(self, city: str) -> dict:
        """Get the weather forecast for a city."""
        url = f"{self.base_url}forecast?q={city}&appid={self.api_key}&units=metric"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        return {}
import os
from typing import Any, Literal, Optional, Dict, List
from dotenv import load_dotenv
# from utils.weather_info import weatherForecastTool
from langchain_core.tools import tool


load_dotenv()  # Load environment variables from .env file
from langchain_groq import ChatGroq


class WeatherInfoTool():

    def __init__(self):
        load_dotenv()  # Ensure environment variables are loaded
        self.api_key = os.getenv("GROQ_API_KEY")
        self.weather_services = WeatherForecastTool(self.api_key)
        self.weather_tool_list = self._setup_tools()

    def _setup_tools(self) -> List:
        """Setup all tools for the weather forecast tool"""
        @tool
        def get_current_weather(city: str) -> str:
            """Get the current weather for a given city."""
            weather_data = self.weather_services.get_current_weather(city)
            if weather_data:
                temp = weather_data.get('main', {}).get('temp', 'N/A')
                desc = weather_data.get('weather', [{}])[0].get('description', 'N/A')
                return f"The current temperature in {city} is {temp}°C with {desc}."
            return f"Could not retrieve weather data for {city}."
        

        @tool
        def get_weather_forecast(city: str) -> str:
            """Get the weather forecast for a city."""
            forecast_data = self.weather_services.get_weather_forecast(city)
            if forecast_data:
                forecasts = []
                for day in forecast_data.get('list', []):
                    date = day.get('dt_txt', 'N/A')
                    temp = day.get('main', {}).get('temp', 'N/A')
                    desc = day.get('weather', [{}])[0].get('description', 'N/A')
                    forecasts.append(f"{date}: {temp}°C with {desc}")
                return "\n".join(forecasts)
            return f"Could not retrieve weather forecast for {city}."
        return [get_current_weather, get_weather_forecast]
import requests
from smolagents import tool
from src.config import WEATHER_TIMEOUT


@tool
def get_weather(city: str) -> str:
    """
    Fetches current weather information for a given city.
    Use this tool when the user asks about weather, temperature,
    or climate conditions in any city.

    Args:
        city: The name of the city to get weather for.
              Examples: 'Helsinki', 'London', 'Karachi'

    Returns:
        A string containing current weather information
        including temperature and conditions.
    """
    try:
        # Detailed weather format
        url = f"https://wttr.in/{city}?format=j1"

        response = requests.get(
            url,
            timeout=WEATHER_TIMEOUT,
            headers={"User-Agent": "WeatherAgent/1.0"}
        )

        if response.status_code == 200:
            data = response.json()
            
            current = data["current_condition"][0]
            temp_c = current["temp_C"]
            feels_like = current["FeelsLikeC"]
            humidity = current["humidity"]
            description = current["weatherDesc"][0]["value"]
            wind_kmph = current["windspeedKmph"]

            return (
                f"Current weather in {city.title()}:\n"
                f"Condition   : {description}\n"
                f"Temperature : {temp_c}°C\n"
                f"Feels Like  : {feels_like}°C\n"
                f"Humidity    : {humidity}%\n"
                f"Wind Speed  : {wind_kmph} km/h\n"
                f"Data source : wttr.in"
            )
        else:
            return f"Could not fetch weather for {city}. Please check the city name."

    except requests.Timeout:
        return f"Request timed out for {city}. Please try again."

    except Exception as e:
        return f"Error fetching weather: {str(e)}"
import aiohttp
import os

WEATHER_API_KEY = os.getenv('WEATHER_API_KEY')


async def get_weather(city_name):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': city_name,
        'appid': WEATHER_API_KEY,
        'units': 'metric',
        'lang': 'ru'
    }

    async with aiohttp.ClientSession() as session:
        async with session.get(base_url, params=params) as response:
            return await response.json()

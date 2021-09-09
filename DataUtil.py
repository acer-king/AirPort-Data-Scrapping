import time
import requests_cache
import json

session = requests_cache.CachedSession('cache', backend='memory')


class DataUtil:
    """
    DataUtil class
    """

    def __init__(self) -> None:
        pass

    @staticmethod
    def get_temperature_from_city_name(city_name):
        """
        get Temperature from City Name
        """
        city_name = city_name.split(' ')[0]
        resp = session.get(
            url="https://community-open-weather-map.p.rapidapi.com/weather",
            params={"q": city_name},
            headers={
                'x-rapidapi-host': 'community-open-weather-map.p.rapidapi.com',
                'x-rapidapi-key': 'f062fd0276msh21c0426a4f59010p173548jsnabed040d747d'
            })
        # convert string to dict variable
        obj = json.loads(resp.content.decode('utf-8'))
        temp = None
        if 'weather' in obj.keys():
            temp = obj['main']['temp'] - 273.15
        return temp

    @staticmethod
    def get_note_from_temperature(temp):
        """
        get note from temperature
        """
        if(temp is None):
            return None
        elif temp > 25:
            return "let's go for a pint"
        elif temp < 5:
            return "so cold"
        else:
            return "normal"

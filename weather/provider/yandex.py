from typing import Self

import requests
from django.conf import settings

from .base import BaseWeatherProvider


class YandexWeatherProvider(BaseWeatherProvider):
    """
    Yandex weather API
    https://yandex.ru/dev/weather/doc/dg/concepts/about.html
    """

    STATUS_OK = 200  # response status code OK

    def __init__(self: Self) -> None:
        self.url = settings.YANDEX_WEATHER_API_ENDPOINT
        self.headers = {
            settings.YANDEX_WEATHER_API_HEADER: settings.YANDEX_WEATHER_API_KEY
        }

    def get_weather_data_by_coordinates(
        self: Self, latitude: float, longitude: float
    ) -> dict:
        payloads = {
            "lat": latitude,
            "lon": longitude,
            "limit": 1,
            "hours": False,
        }
        response = requests.get(
            self.url, params=payloads, headers=self.headers, timeout=5
        )
        weather_data = response.json()
        if response.status_code == self.STATUS_OK:
            return {
                "temperature": weather_data["fact"]["temp"],
                "wind_speed": weather_data["fact"]["wind_speed"],
                "pressure": weather_data["fact"]["pressure_mm"],
            }
        return {}

from typing import Self

from rest_framework.fields import SerializerMethodField
from rest_framework.serializers import ModelSerializer

from .models import City
from .provider.yandex import YandexWeatherProvider


class CitySerializer(ModelSerializer):
    weather = SerializerMethodField("get_weather")

    def get_weather(self: Self, obj: City) -> dict:
        provider = YandexWeatherProvider()
        return provider.get_weather_data_by_coordinates(
            latitude=obj.latitude, longitude=obj.longitude
        )

    class Meta:
        model = City
        fields = (
            "name",
            "latitude",
            "longitude",
            "weather",
        )

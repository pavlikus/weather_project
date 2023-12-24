from abc import ABC
from abc import abstractmethod
from typing import Self


class BaseWeatherProvider(ABC):
    @abstractmethod
    def get_weather_data_by_coordinates(
        self: Self, latitude: float, longitude: float
    ) -> dict:
        raise NotImplementedError

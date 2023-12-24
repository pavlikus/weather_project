from random import randint
from typing import Self
from unittest import mock

import pytest
from django.core.cache import cache
from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from weather.models import City


class WeatherAPITest(APITestCase):
    fixtures = ["cities"]

    def setUp(self: Self) -> None:
        self.client = APIClient()
        self.url = reverse("weather")

    @pytest.mark.run(order=1)
    def test_empty_cache(self: Self) -> None:
        assert len(cache._cache) == 0

    @pytest.mark.run(order=2)
    def test_bad_request(self: Self) -> None:
        response = self.client.get(self.url)
        assert response.status_code == 400

    @mock.patch(
        "weather.serializers.CitySerializer.get_weather",
        return_value={
            "temperature": 0,
            "wind_speed": 0,
            "pressure": 0,
        },
    )
    @pytest.mark.run(order=3)
    def test_ok_request(self: Self, *args) -> None:  # noqa
        total = City.objects.count()
        pk = randint(1, total)
        city = City.objects.get(pk=pk)
        response = self.client.get(self.url, data={"city": city.name})
        assert response.status_code == 200
        assert response.data["name"] == city.name

    @mock.patch(
        "weather.serializers.CitySerializer.get_weather",
        return_value={
            "temperature": 100,
            "wind_speed": 0,
            "pressure": 0,
        },
    )
    @pytest.mark.run(order=4)
    def test_mock_ok_request(self: Self, *args) -> None:  # noqa
        total = City.objects.count()
        pk = randint(1, total)
        city = City.objects.get(pk=pk)
        response = self.client.get(self.url, data={"city": city.name})
        assert response.status_code == 200
        assert response.data["weather"]["temperature"] == 100

    @pytest.mark.run(order=5)
    def test_not_found_request(self: Self) -> None:
        response = self.client.get(self.url, data={"city": "test"})
        assert response.status_code == 404

    @pytest.mark.run(order=6)
    def test_not_empty_cache(self: Self) -> None:
        assert len(cache._cache) > 1

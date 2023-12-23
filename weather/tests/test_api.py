from random import randint
from typing import Self

from rest_framework.reverse import reverse
from rest_framework.test import APIClient
from rest_framework.test import APITestCase

from weather.models import City


class WeatherAPITest(APITestCase):
    fixtures = ["cities"]

    def setUp(self: Self) -> None:
        self.client = APIClient()
        self.url = reverse("weather")

    def test_bad_request(self: Self) -> None:
        response = self.client.get(self.url)
        assert response.status_code == 400

    def test_ok_request(self: Self) -> None:
        total = City.objects.count()
        pk = randint(0, total)
        city = City.objects.get(pk=pk)
        response = self.client.get(self.url, data={"city": city.name})
        assert response.status_code == 200
        assert response.data["name"] == city.name

    def test_not_found_request(self: Self) -> None:
        response = self.client.get(self.url, data={"city": "test"})
        assert response.status_code == 404

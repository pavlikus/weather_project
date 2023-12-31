from typing import Self

from django.conf import settings
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import City
from .serializers import CitySerializer


class CityAPIView(APIView):
    def get_object(self: Self, name: str) -> City:
        return get_object_or_404(City, name__iexact=name)

    @method_decorator(cache_page(settings.API_CACHE_TIME))
    def get(self: Self, request: Request) -> Response:
        city_name = request.GET.get("city", None)
        if city_name is not None:
            obj = self.get_object(city_name)
            serializer = CitySerializer(obj)
            return Response(serializer.data)
        return Response(status=status.HTTP_400_BAD_REQUEST)

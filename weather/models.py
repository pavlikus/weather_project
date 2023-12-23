from typing import Self

from django.db import models


class City(models.Model):
    """
    TODO: add GIS system(DB based on GIS) if necessary
    https://docs.djangoproject.com/en/5.0/ref/contrib/gis/
    """

    name = models.CharField(max_length=128, unique=True, db_index=True)
    latitude = models.FloatField()
    longitude = models.FloatField()

    def __str__(self: Self) -> str:
        return self.name

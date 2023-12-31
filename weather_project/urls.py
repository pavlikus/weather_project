from django.conf import settings
from django.contrib import admin
from django.urls import include
from django.urls import path

from weather.views import CityAPIView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/weather/", CityAPIView.as_view(), name="weather"),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    import debug_toolbar

    urlpatterns += [
        path("__debug__/", include(debug_toolbar.urls)),
        *static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT),
    ]

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "weather_project.settings")
os.environ.setdefault("DJANGO_CONFIGURATION", "Production")

application = get_wsgi_application()

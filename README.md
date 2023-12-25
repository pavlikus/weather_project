# Simple Weather Project

Service for getting weather data

## Instruction
Required **python>=3.11**

First of all you need clone this project and create environment.
```bash
git clone https://github.com/pavlikus/weather_project
python -m venv env
source env/bin/activate
cd weather_project
```
Create ```.env``` file and add
```
DJANGO_CONFIGURATION=Production
SECRET_KEY=secret
YANDEX_WEATHER_API_KEY=
TELEGRAM_BOT_TOKEN=
```
After that please install requirements
```bash
pip install -r requirements/production.txt
```
Create DB structure
```bash
python manage.py migrate
```
Install russian cities dataset
```bash
python manage.py loaddata cities
```

### Run server
```bash
python manage.py runserver
```

### Run bot
```bash
python manage.py runbot
```

### Run test
```bash
pip install -r requirements/test.txt
python manage.py test
```

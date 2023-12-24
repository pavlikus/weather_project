import telebot
from django.conf import settings
from django.core.management import BaseCommand

from weather.models import City
from weather.provider.yandex import YandexWeatherProvider

bot = telebot.TeleBot(settings.TELEGRAM_BOT_TOKEN)


class Command(BaseCommand):
    help = "Run Weather Forecast Telegram bot."  # noqa

    def handle(self, *args, **kwargs):  # noqa
        @bot.message_handler(content_types=["text"])
        def start(message):  # noqa
            msg = bot.send_message(
                message.chat.id,
                (
                    "Welcome to Weather Forecast bot. "
                    "Please enter your city"
                    "(only Russian city and letters allowed)?"
                ),
            )
            bot.register_next_step_handler(msg, get_weather_data)

        def get_weather_data(message):  # noqa
            city_name = message.text
            city = City.objects.filter(name__iexact=city_name).first()
            if city:
                provider = YandexWeatherProvider()
                weather = provider.get_weather_data_by_coordinates(
                    latitude=city.latitude, longitude=city.longitude
                )
                bot.send_message(
                    message.chat.id,
                    (
                        f"Today in {city.name}.\n"
                        f"Temperature: {weather['temperature']} ℃\n"
                        f"Wind Speed: {weather['wind_speed']} m/s\n"
                        f"Pressure: {weather['pressure']} mm Hg"
                    ),
                )
            else:
                bot.send_message(
                    message.chat.id,
                    f"Sorry I can't find {city_name} in my base!",
                )

        bot.infinity_polling()

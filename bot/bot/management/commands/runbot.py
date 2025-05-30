from django.core.management.base import BaseCommand
from bot.telegram.app import start_bot

class Command(BaseCommand):
    help = "Запуск Telegram-бота"

    def handle(self, *args, **kwargs):
        start_bot()

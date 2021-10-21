from django.core.management.base import BaseCommand
from telegram.ext import Updater, CommandHandler, MessageHandler
from ...views import start


TOKEN = "1935935887:AAFfDELqK7nAO0T13WqFDiaeCELz1XkAS20"
class Command(BaseCommand):

    def handle(self, *args, **options):

        updater = Updater(TOKEN)
        updater.dispatcher.add_handler(CommandHandler("start", start))

        updater.start_polling()
        updater.idle()

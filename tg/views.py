from django.shortcuts import render
from telegram.ext import Updater
from telegram import Update


def start(update,context):
    user = update.message.from_user
    update.message.reply_text(f"hello {user.first_name} --- {user.id}")
import os

from dotenv import load_dotenv

import telebot

load_dotenv()

TELEGRAM_BOT_TOKEN = os.environ.get('TELEGRAM_BOT_TOKEN')  # Here is your's TELEGRAM BOT API TOKEN


bot = telebot.TeleBot(TELEGRAM_BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    chat_id = message.chat.id
    bot.send_message(chat_id, "Напишите сообщение, оно будет сразу отправлено админу")


bot.polling()

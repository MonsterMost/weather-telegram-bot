from telebot import TeleBot
from bs4 import BeautifulSoup
import requests
import config

bot = TeleBot(config.TOKEN)


@bot.message_handler(commands=['start'])  # Чтобы реагировал на старт
def command_start(message):  # всегда принимает мэссэдж
    chat_id = message.chat.id  # Берем чат айди
    bot.send_message(chat_id,
                     f'Привет, {message.from_user.first_name}!\nЭто Автоотправитель-бот!')
    # Отправляем тому, что написал обратно сообщение
    send_photo(message)


def send_photo(message):
    bot.send_photo(config.CHANNEL_ID, '')


print('Бот работает!')
bot.polling(none_stop=True)

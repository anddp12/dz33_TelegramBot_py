import telebot
from config import BOT_TOKEN
import json


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}\nИграем в игру города Украины.\nДля старта введите название города.".format(message.from_user))


with open("city_Ukr.json", 'r', encoding='utf-8') as f:
    data = json.load(f)


@bot.message_handler(content_types=['text'])
def echo_message(message):
    if message.text in data:
        data.remove(message.text)

        for i in data:
            if str(message.text[-1]).upper() == str(i[0]).upper():
                bot.send_message(message.chat.id,i)
                data.remove(i)
                break
    else:
        bot.send_message(message.chat.id, "Слово задублировано")


bot.infinity_polling()
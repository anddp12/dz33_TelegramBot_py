import telebot
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, text="Привет, {0.first_name}\nИграем в игру города.".format(message.from_user))


bot.infinity_polling()
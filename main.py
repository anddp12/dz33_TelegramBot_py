import telebot
from config import BOT_TOKEN


bot = telebot.TeleBot(BOT_TOKEN)


if __name__ == '__main__':
    bot.infinity_polling()
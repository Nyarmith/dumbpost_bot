import telebot
import random
from datetime import datetime
import trash_parser

bot = telebot.TeleBot("secret key")

p=0.2


@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.send_message(message.chat.id, trash_parser.genSentence())

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    random.seed(datetime.now())
    if (random.random() > p):
        bot.send_message(message.chat.id, trash_parser.genSentence())

bot.polling()

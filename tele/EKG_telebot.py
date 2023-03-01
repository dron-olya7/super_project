import pyautogui
import telebot
import numexpr as ne
from telebot import types
import os
import cv2
import platform
import requests
import pyautogui as pag
import matplotlib
from IPython.display import display
import matplotlib.pyplot as plt
#%matplotlib inline
import numpy as np
#import os
import shutil
import posixpath
import wfdb


TOKEN = "5501433938:AAEFl5ZvofaPuILEdc0fZkWaKrd1MyHwUpk"
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['system', 'start'])
def system(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = [wfdb.get_record_list('mitdb')]
    markup.row(*buttons[0])
    bot.send_message(message.chat.id,
                     """Выберите номер графика:""",
                     reply_markup=markup
                     )

@bot.message_handler()
def get_user_text(message):
    print(message.from_user.id, message.from_user.username, message.text)
    try:
        answer = message.text
        record = wfdb.rdrecord(answer, pn_dir='mitdb/1.0.0', sampto=1000)
        fig=wfdb.plot.plot_wfdb(record=record, title='Record ' + answer + ' from PhysioNet mitdb', return_fig=True)
        filename='saved_figure.png'
        fig.savefig(filename)
        with open(filename, "rb") as img:
            bot.send_photo(message.chat.id, img)
        os.remove(filename)
    except:
        if message.text == "привет":
            bot.send_message(message.chat.id, "И тебе привет!", parse_mode='html')
        elif message.text == "id":
            bot.send_message(message.chat.id, f"Твой ID: {message.from_user.id}", parse_mode='html')
        elif message.text == "photo":
            bot.send_photo(message.chat.id,
                           'https://upload.wikimedia.org/wikipedia/commons/e/e1/Wilson_%22Snowflake%22_Bentley.jpg')
        else:
            bot.send_message(message.chat.id, f"Я тебя не понимаю, {message.from_user.first_name}", parse_mode='html')


@bot.message_handler(content_types=['sticker'])
def get_user_sticker(message):
    bot.send_sticker(message.chat.id, 'CAACAgIAAxkBAAEEo3xidOdOyeO38Wupmd1WPfI19iGj4QACOwMAArVx2gYYSwbSVVPLRCQE')


bot.polling(none_stop='true')
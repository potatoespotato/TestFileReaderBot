# -*- coding: utf-8 -*-
import telebot

from text_reader import File_reader
from words import Porter # оставляет только корень слова (не очень точный код)






token = '686815651:AAGBhecqUXjlRz5CHQFzhK8SlFZE8dXv4Jc'
bot = telebot.TeleBot(token)


keyboard = telebot.types.ReplyKeyboardMarkup() # создание кнопки
keyboard.row('Искать в папке')

reader = File_reader()

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, 'Введите ключевые слова через пробел', reply_markup=keyboard)


@bot.message_handler(content_types=['text'])
def send_files(message):
    print(message.text)
    if message.text != 'Искать в папке':
        words = message.text.split()
        right_words = []
        for word in words:
            right_words.append(Porter.stem(word))
        if right_words:
            files = reader.searh(right_words)
            print(right_words)
        for file in files:
            doc = open(file[:-4], 'rb')
            bot.send_photo(message.chat.id, doc, reply_markup=keyboard)
    else:
        bot.send_message(message.chat.id, 'Введите ключевые слова через пробел', reply_markup=keyboard)
        
bot.polling()

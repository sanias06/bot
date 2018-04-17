import minc
import telebot
from telebot import types
from flask import Flask
from flask import request
from flask import jsonify


token = minc.token
bot = telebot.TeleBot(token)
app = Flask(__name__)

import pots

@app.route('/', methods=['POST','GET'])
def index():



    if request.method == 'POST':
        r = request.get_json()
        chat_id = r['message']['chat']['id']
        text = r['message']['text']

        if text == '/last_add':
            txt = pots.last_add()
            bot.send_message(chat_id, txt)

        if text == '/homework':
            markup = types.ReplyKeyboardMarkup()
            markup.row('пн', 'вт', 'ср')
            markup.row('чт', 'пт', 'сб')
            markup.row('сегодня')
            markup.row('завтра')
            bot.send_message(chat_id, 'Выберите день недели:', reply_markup=markup)

        if text == '/timetable':
            markup = types.ReplyKeyboardMarkup()
            markup.row('Пн', 'Вт', 'Ср')
            markup.row('Чт', 'Пт', 'Сб')
            markup.row('Сегодня')
            markup.row('Завтра')
            bot.send_message(chat_id, 'Выберите день недели:', reply_markup=markup)

        if text == 'пн':
            txt = pots.parse_homework(0)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'вт':
            txt = pots.parse_homework(1)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'ср':
            txt = pots.parse_homework(2)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'чт':
            txt = pots.parse_homework(3)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'пт':
            txt = pots.parse_homework(4)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'сб':
            txt = pots.parse_homework(5)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'сегодня':
            txt = pots.parse_homework(pots.today_tomorow(0))
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'завтра':
            txt = pots.parse_homework(pots.today_tomorow(1))
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)

        if text == 'Пн':
            txt = pots.parse_tt(0)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'Вт':
            txt = pots.parse_tt(1)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'Ср':
            txt = pots.parse_tt(2)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'Чт':
            txt = pots.parse_tt(3)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'Пт':
            txt = pots.parse_tt(4)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'Сб':
            txt = pots.parse_tt(5)
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'Сегодня':
            txt = pots.parse_tt(pots.today_tomorow(0))
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)
        if text == 'Завтра':
            txt = pots.parse_tt(pots.today_tomorow(1))
            p = types.ReplyKeyboardRemove()
            bot.send_message(chat_id, txt, reply_markup=p)

        return jsonify(r)



    return '<h1>ZHEZH LOX</h1>'




if __name__ == '__main__':
    app.run()
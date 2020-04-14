import telebot
from telebot.types import Message
from telebot import types
import random
import requests
from telebot import types
from time import sleep
import datetime
import schedule
import time
import urllib.request

list_1 = ['https://ibb.co/qkfxwfs', 'https://ibb.co/t380NNg', 'https://ibb.co/Bcj7x0H']

# Подключение
TOKEN = "1007614975:AAGQ_bTc8P9nJUZKdqkWsQlQ4lBth4ONLig"
url = "https://api.telegram.org/bot1007614975:AAGQ_bTc8P9nJUZKdqkWsQlQ4lBth4ONLig/"
bot = telebot.TeleBot(TOKEN)


# Получение обновленй
class BotHandler:

    def __init__(self, token):
        self.token = token
        self.api_url = "https://api.telegram.org/bot{}/".format(token)

    def get_updates(self, offset=None, timeout=30):
        method = 'getUpdates'
        params = {'timeout': timeout, 'offset': offset}
        resp = requests.get(self.api_url + method, params)
        result_json = resp.json()['result']
        return result_json

    def send_message(self, chat_id, text):
        params = {'chat_id': chat_id, 'text': text}
        method = 'sendMessage'
        resp = requests.post(self.api_url + method, params)
        return resp

    def get_last_update(self):
        get_result = self.get_updates()

        if len(get_result) > 0:
            last_update = get_result[-1]
        else:
            last_update = get_result[len(get_result)]

        return last_update

# Функции
m16 = [10, 11, 12, 13, 14, 15]
c16 = ['A', 'B', 'C', 'D', 'E', 'F']
k = []
def TenSS(x1,x2):
    # Начальная система счисления 10, преревод с любыми СС(Кроме 16)
    k = []
    b = x1
    c = x2
    while b != 0:
        if b % c in m16:
            for i in range(len(m16)):
                if m16[i] == b % c:
                    k.append(c16[i])
                    break
        else:
            k.append(str(b % c))
        b //= c
    k.reverse()
    s = ''.join(k)
    return s


def SSTen(x1, x2):
    # Начальная система счисления x, преревод в 10-ую СС
    b = x1
    c = x2
    s = 0
    st = 1
    for i in range(1, len(b) + 1):
        if b[-i] in c16:
            for j in range(len(c16)):
                if c16[j] == b[-i]:
                    s += int(m16[j]) * st
                    break
        else:
            s += int(b[-i]) * st
        st *= c
    return s


smile = [
    '❤',
]


@bot.message_handler(commands=['help'])
def help(message):
    bot.send_message(message.chat.id, "/start - Отправка заданий/n /help - Помощь/n /url - Ссылки на важную информацию")
def mess(b,d,c):
    flag = True
    while flag:
        kol = 0
        for i in b:
            if i in c16:
                for j in range(len(c16)):
                    if i == c16[j]:
                        i = m16[j]
                        break
            if int(i) >= d:
                return ('Число некорректное, введите число еще раз')
                break
            kol += 1
        if kol == len(b):
            flag = False
    if d == 10:
        b = int(b)
        return TenSS(b, c)
    elif c == 10:
        return SSTen(b, d)
    else:
        return TenSS(SSTen(b, d), c)

# Ссылки на сайты
@bot.message_handler(commands=['url'])
def url(message):
    markup001 = types.InlineKeyboardMarkup()
    btn_may_group = types.InlineKeyboardButton(text="Группа Квентина", url="https://vk.com/chbquentin")
    markup001.add(btn_may_group)
    bot.send_message(message.chat.id, "Перейди по ссылке", reply_markup=markup001)
    markup002 = types.InlineKeyboardMarkup()
    site_python = types.InlineKeyboardButton(text="Методичка по python",
                                             url="https://docs.python.org/3/tutorial/index.html")
    markup002.add(site_python)
    bot.send_message(message.chat.id, "Перейди по ссылке", reply_markup=markup002)
    markup003 = types.InlineKeyboardMarkup()
    site_C = types.InlineKeyboardButton(text="Методичка по C++",
                                        url="https://www.rulit.me/books/c-bazovyj-kurs-read-271738-1.html")
    markup003.add(site_C)
    bot.send_message(message.chat.id, "Перейди по ссылке", reply_markup=markup003)



# Действующие кнопки
@bot.message_handler(commands=['start'])
def send_welcome(message: Message):
    bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=Keyboard())
# отправка методички
@bot.message_handler(content_types=['text'])
def text(message):
    if message.text == "Калькулятор":
        bot.send_message(message.chat.id, "1)Введите число\n 2)Введите в какой СС число\n 3)В какую СС перевести\n (Запишите в одну строчку через пробел)")
    elif len(message.text.split(" ")) == 3:
        line = message.text
        b = line.split(" ")[0]
        d = int(line.split(" ")[1])
        c = int(line.split(" ")[2])
        bot.send_message(message.chat.id, mess(b, d, c))
    elif message.text == "Задания":
        bot.send_message(message.chat.id, "Выберите часть: ", reply_markup=Keyboard1())
    elif message.text == "Часть 1":
        bot.send_message(message.chat.id, "Выберите задания: ", reply_markup=Keyboard2())
    elif message.text == "Задания 1-11":
        bot.send_message(message.chat.id, " Выберите задание: ", reply_markup=Keyboard3())
    elif message.text == "Задание 10":
        img1 = ('https://i.ibb.co/XLKhxzd/10-a.jpg')
        img2 = ('https://i.ibb.co/zmqvCr6/10.png')
        media = [types.InputMediaPhoto(img1, "1"), types.InputMediaPhoto(img2, "2")]
        bot.send_media_group(message.chat.id, media)
    elif message.text == "Задание 9":
        img3 = ("https://i.ibb.co/xgFbTYy/9-a.jpg")
        img4 = ('https://i.ibb.co/QDj3RPB/9.jpg')
        img5 = ('https://i.ibb.co/3WFvbWH/9.jpg')
        media = [types.InputMediaPhoto(img3, "1"), types.InputMediaPhoto(img4, "2"), types.InputMediaPhoto(img5, "3")]
        bot.send_media_group(message.chat.id, media)
    elif message.text == "Задания 12-22":
        bot.send_message(message.chat.id, " Выберите задание: ", reply_markup=Keyboard4())
    elif message.text == "Часть 2":
        bot.send_message(message.chat.id, "Выберите задания: ", reply_markup=Keyboard5())
    elif message.text == "Задание 16":
        img6 = ("https://i.ibb.co/FJvLNxr/zadanie-16-1.jpg")
        img7 = ("https://i.ibb.co/VTN1kVz/zadanie-16-2.jpg")
        img8 = ("https://i.ibb.co/W20GjLD/zadanie-16-3.jpg")
        img9 = ("https://i.ibb.co/V9R4XtG/zadanie-16-4.jpg")
        media = [types.InputMediaPhoto(img6, '1'), types.InputMediaPhoto(img7, '2'), types.InputMediaPhoto(img8, '3'),
                 types.InputMediaPhoto(img9, '4')]
        bot.send_media_group(message.chat.id, media)
    elif message.text == "Задание 26":
        img10 = ('https://i.ibb.co/RCG89G0/26-a.jpg')
        img11 = ('https://i.ibb.co/kyfyVpL/26.jpg')
        img12 = ('https://i.ibb.co/PzhRCHX/26.jpg')
        img13 = ('https://i.ibb.co/bsPHLYQ/26.jpg')
        img14 = ('https://i.ibb.co/jhf6b3d/26.jpg')
        img15 = ('https://i.ibb.co/fq30dn4/26.jpg')
        img16 = ('https://i.ibb.co/FX7qszy/26.jpg')
        img17 = ('https://i.ibb.co/M2RVH1y/26.jpg')
        img18 = ('https://i.ibb.co/3BvKsKV/26.jpg')
        media = [types.InputMediaPhoto(img10, "1"), types.InputMediaPhoto(img11, "2"),
                 types.InputMediaPhoto(img12, "3"),
                 types.InputMediaPhoto(img13, "4"), types.InputMediaPhoto(img14, "5"),
                 types.InputMediaPhoto(img15, "6"),
                 types.InputMediaPhoto(img16, "7"), types.InputMediaPhoto(img17, "8"),
                 types.InputMediaPhoto(img18, "9")]
        bot.send_media_group(message.chat.id, media)
    elif message.text == "Задание 18":
        img19 = ('https://i.ibb.co/dJFsJmQ/ddfa3fdfe08fc21b94edd988f806b714-0.jpg')
        img20 = ('https://i.ibb.co/K6rxKGh/ddfa3fdfe08fc21b94edd988f806b714-1.jpg')
        img21 = ('https://i.ibb.co/7RzP94s/ddfa3fdfe08fc21b94edd988f806b714-2.jpg')
        img22 = ('https://i.ibb.co/XCz876b/ddfa3fdfe08fc21b94edd988f806b714-3.jpg')
        img23 = ('https://i.ibb.co/x1CgNJV/ddfa3fdfe08fc21b94edd988f806b714-4.jpg')
        media = [types.InputMediaPhoto(img19, "1"), types.InputMediaPhoto(img20, "2"),
                 types.InputMediaPhoto(img21, "3"),
                 types.InputMediaPhoto(img22, "4"), types.InputMediaPhoto(img23, "5")]
        bot.send_media_group(message.chat.id, media)
    elif message.text == "Стартовое меню":
        bot.send_message(message.chat.id, "Добро пожаловать", reply_markup=Keyboard())


# Клавиатура
def Keyboard():
    markup = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    button_1 = types.KeyboardButton("Задания")
    button_2 = types.KeyboardButton("Методичка по программированию")
    button_ki = types.KeyboardButton("Калькулятор")
    markup.add(button_1, button_2, button_ki)
    return markup


def Keyboard1():
    markup1 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    button_3 = types.KeyboardButton("Часть 1")
    button_4 = types.KeyboardButton("Часть 2")
    button_0 = types.KeyboardButton("Стартовое меню")
    markup1.add(button_3, button_4, button_0)
    return markup1


def Keyboard2():
    markup2 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    button_5 = types.KeyboardButton("Задания 1-11")
    button_6 = types.KeyboardButton("Задания 12-22")
    button_03 = types.KeyboardButton("Стартовое меню")
    markup2.add(button_5, button_6, button_03)
    return markup2


def Keyboard3():
    markup3 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    button_7 = types.KeyboardButton("Задание 1")
    button_8 = types.KeyboardButton("Задание 2")
    button_9 = types.KeyboardButton("Задание 3")
    button_10 = types.KeyboardButton("Задание 4")
    button_11 = types.KeyboardButton("Задание 5")
    button_12 = types.KeyboardButton("Задание 6")
    button_13 = types.KeyboardButton("Задание 7")
    button_14 = types.KeyboardButton("Задание 8")
    button_15 = types.KeyboardButton("Задание 9")
    button_16 = types.KeyboardButton("Задание 10")
    button_17 = types.KeyboardButton("Задание 11")
    button_02 = types.KeyboardButton("Стартовое меню")
    markup3.add(button_7, button_8, button_9, button_10, button_11, button_12,
                button_13, button_14, button_15, button_16, button_17, button_02)
    return markup3


def Keyboard4():
    markup4 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    button_18 = types.KeyboardButton("Задание 12")
    button_19 = types.KeyboardButton("Задание 13")
    button_20 = types.KeyboardButton("Задание 14")
    button_21 = types.KeyboardButton("Задание 15")
    button_22 = types.KeyboardButton("Задание 16")
    button_23 = types.KeyboardButton("Задание 17")
    button_24 = types.KeyboardButton("Задание 18")
    button_25 = types.KeyboardButton("Задание 19")
    button_26 = types.KeyboardButton("Задание 20")
    button_27 = types.KeyboardButton("Задание 21")
    button_28 = types.KeyboardButton("Задание 22")
    button_01 = types.KeyboardButton("Стартовое меню")
    markup4.add(button_18, button_19, button_20, button_21, button_22, button_23,
                button_24, button_25, button_26, button_27, button_28, button_01)
    return markup4


def Keyboard5():
    markup5 = types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True, row_width=3)
    button_29 = types.KeyboardButton("Задание 23")
    button_30 = types.KeyboardButton("Задание 24")
    button_31 = types.KeyboardButton("Задание 25")
    button_32 = types.KeyboardButton("Задание 26")
    button_33 = types.KeyboardButton("Задание 27")
    button_34 = types.KeyboardButton("Стартовое меню")
    markup5.add(button_29, button_30, button_31, button_32, button_33, button_34)
    return markup5

'''
# Отправка сообщений каждый четверг в 17:00
def job():
    bot.send_message(701090458,
                     'Ребятки, сегодня последний срок сдачи домашнего задания. Не забываем) С любовью, Кристина.')
    bot.send_message(266187636,
                     'Ребятки, сегодня последний срок сдачи домашнего задания. Не забываем) С любовью, Кристина.')
    bot.send_message(998634637,
                     'Ребятки, сегодня последний срок сдачи домашнего задания. Не забываем) С любовью, Кристина.')


schedule.every().saturday.at("22:28").do(job)
while True:
    schedule.run_pending()
    time.sleep(1)


# отправка сообщений каждый понедельник
def msg():
    bot.send_message(701090458,
                     'Хей, ребятки. Милые последователи, Кристины❤️. Не забываем сделать дз до пятницы. Не будем расстраивать нашу Кристину😌')
    bot.send_message(266187636,
                     "Хей, ребятки. Милые последователи, Кристины❤️. Не забываем сделать дз до пятницы. Не будем расстраивать нашу Кристину😌")
    bot.send_message(998634637,
                     "Хей, ребятки. Милые последователи, Кристины❤️. Не забываем сделать дз до пятницы. Не будем расстраивать нашу Кристину😌")


schedule.every().saturday.at("22:05").do(msg)
# schedule.every().monday.at("17:00").do(msg)
# schedule.every().tuesday.at("17:00").do(msg)
# schedule.every().wednesday.at("17:00").do(msg)
while True:
    schedule.run_pending()
    time.sleep(1)
'''
bot.polling()

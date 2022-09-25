import telebot
from telebot import types # для указание типов
#import config
from bot_token import bot_one as bot

#bot = telebot.TeleBot(config.token)
def send(id,text):
    bot.send_message(id, text)
    print(id)

@bot.message_handler(commands=['start'])
def start(message):
    sti = open('gerl.webp', 'rb')
    bot.send_sticker(message.chat.id, sti)
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)

    btn1 = types.KeyboardButton("👋 Узнать адрес и телефон")
    btn2 = types.KeyboardButton("❓ Задать вопрос")
    markup.add(btn1, btn2)
    bot.send_message(message.chat.id, text="Привет, {0.first_name}! Я тестовый бот мебельного магазина (ваш магазин)".format(message.from_user), reply_markup=markup)
    
    
#СОЗДАНИЕ КНОПОК
@bot.message_handler(commands=['websaite'])
def webst(message):
    marku = types.InlineKeyboardMarkup()
    marku.add(types.InlineKeyboardButton("Посетить веб сайт",url="https://www.moysaitvilozhiegonahost.com"))
    bot.send_message(message.chat.id, 'Перейди на вебсайт', reply_markup=marku)
    
 @bot.message_handler(content_types=['text'])
def func(message):
    if(message.text == "👋 Узнать адрес и телефон"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        bot1 = types.KeyboardButton("Узнать номер телефона?")
        bot2 = types.KeyboardButton("Узнать адрес?")
        markup.add(bot1, bot2)
        bot.send_message(message.chat.id, text="Добро пожаловать, {0.first_name}\nЯ - <b>{1.first_name}</b>, бот созданный чтобы".format(message.from_user, bot.get_me(), reply_markup= markup))

    elif(message.text == "❓ Задать вопрос"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        btn1 = types.KeyboardButton("Какой ассортимент мебели?")
        btn2 = types.KeyboardButton("Кухни на заказ")
        back = types.KeyboardButton("Вернуться в главное меню")
        markup.add(btn1, btn2, back)
        bot.send_message(message.chat.id, text="Задай мне вопрос", reply_markup=markup)

    elif(message.text == "Какой ассортимент мебели и дизайна?"):
        bot.send_message(message.chat.id, "Вся мебель изготавливается индивидуально под вас, но есть и в наличии")

    elif message.text == "Кухни на заказ":
        bot.send_message(message.chat.id, text="Вы можете приехать по адресу и выбрать подходящий вам дизайн")

    elif (message.text == "Вернуться в главное меню"):
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        button1 = types.KeyboardButton("👋 Узнать адрес и телефон")
        button2 = types.KeyboardButton("❓ Задать вопрос")
        markup.add(button1, button2)
        bot.send_message(message.chat.id, text="Вы вернулись в главное меню", reply_markup=markup)
    else:
        bot.send_message(message.chat.id, text="На такую комманду я не запрограммирован,.. Напиши еще раз")



bot.polling(none_stop=True)

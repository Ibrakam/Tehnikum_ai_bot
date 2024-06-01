import telebot
from dotenv import dotenv_values

import buttons
from our_ai import *

config_token = dotenv_values(".env")
bot_token = config_token['BOT_TOKEN']
bot = telebot.TeleBot(bot_token)


@bot.message_handler(commands=['start'])
def start(message):
    user_id = message.from_user.id
    bot.send_message(chat_id=user_id, text="Выберите действие в меню: ", reply_markup=buttons.main_menu_bt())


@bot.message_handler(content_types=["text"])
def text_handler(message):
    user_id = message.from_user.id
    if message.text == "💬Задать вопрос":
        bot.send_message(chat_id=user_id, text="Задайте свой вопрос",
                         reply_markup=buttons.cancel_kb())
        bot.register_next_step_handler(message, generate_answer)
    elif message.text == "🌅Сгенерировать изображение":
        bot.send_message(chat_id=user_id, text="Введите текст по которому вы хотите сгенерировать изображение",
                         reply_markup=buttons.cancel_kb())
        bot.register_next_step_handler(message, generate_image)
    elif message.text == "❌Отменить":
        bot.send_message(chat_id=user_id, text="Выберите действие в меню: ",
                         reply_markup=buttons.main_menu_bt())


def generate_answer(message):
    user_id = message.from_user.id
    text = message.text
    answer = chat_gpt3(text)
    bot.send_message(chat_id=user_id, text=answer, reply_markup=buttons.main_menu_bt())


def generate_image(message):
    user_id = message.from_user.id
    text = message.text
    image = text_to_picture(text)
    bot.send_photo(chat_id=user_id, photo=image, reply_markup=buttons.main_menu_bt())


bot.infinity_polling()

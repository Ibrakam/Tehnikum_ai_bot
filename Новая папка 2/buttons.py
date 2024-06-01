from telebot.types import ReplyKeyboardMarkup, KeyboardButton

def main_menu_bt():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    gpt3 = KeyboardButton(text="💬Задать вопрос")
    dalle = KeyboardButton(text="🌅Сгенерировать изображение")
    kb.add(gpt3, dalle)
    return kb

def cancel_kb():
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    cancel = KeyboardButton(text="❌Отменить")
    kb.add(cancel)
    return kb

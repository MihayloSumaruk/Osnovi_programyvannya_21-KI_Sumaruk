from telebot import TeleBot
def deco(funk):
    def wrapper(*args, **kwargs):
        funk(*args, **kwargs)
        print("Бот готовий до роботи !")
    return wrapper
@deco
def start(bot: TeleBot, message):
    bot.send_message(
        message.chat.id,
        "Радий вітати вас! Я WIKI-Telegram Бот, який допоможе вам з освоєнням DotaBuff. Для початку виберіть своє звання. Використайте команду /ranked"
    )
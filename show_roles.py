from telebot import types, TeleBot

def show_roles(bot: TeleBot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.row(types.KeyboardButton("Carry"), types.KeyboardButton("Mid"), types.KeyboardButton("Offlaner"))
    markup.row(types.KeyboardButton("Soft Support"), types.KeyboardButton("Hard Support"))
    markup.row(types.KeyboardButton("Назад"))
    bot.send_message(message.chat.id, "Виберіть вашу роль:", reply_markup=markup)
from telebot import types, TeleBot

def ranked(bot: TeleBot, message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    ranks = ["Herald", "Guardian", "Crusader", "Archon", "Legend", "Ancient", "Divine", "Immortal"]
    for i in range(0, len(ranks), 2):
        markup.row(types.KeyboardButton(ranks[i]), types.KeyboardButton(ranks[i+1]))
    bot.send_message(message.chat.id, "Виберіть ваше звання:", reply_markup=markup)
from telebot import TeleBot
from handlers.show_roles import show_roles
from handlers.gen_url import generate_url

def process_text(bot: TeleBot, message, user_states):
    ranks_url_map = {
        "Herald": "herald", "Guardian": "guardian", "Crusader": "crusader",
        "Archon": "archon", "Legend": "legend", "Ancient": "ancient",
        "Divine": "divine", "Immortal": "immortal"
    }
    roles_url_map = {
        "Carry": "core-safe", "Mid": "core-mid", "Offlaner": "core-off",
        "Soft Support": "support-safe", "Hard Support": "support-off"
    }

    ranks = list(ranks_url_map.keys())
    roles = list(roles_url_map.keys())

    if message.text in ranks:
        user_states[message.chat.id] = {'rank': message.text, 'role': None}
        bot.send_message(message.chat.id, f"Ваше звання: {message.text}")
        show_roles(bot, message)
    elif message.text in roles:
        if message.chat.id in user_states and user_states[message.chat.id]['rank']:
            user_states[message.chat.id]['role'] = message.text
            rank = user_states[message.chat.id]['rank']
            role = message.text
            url = generate_url(rank, role)
            bot.send_message(message.chat.id, f"Ось стаття яка допоможе вам ознайомитись: {url}")
        else:
            bot.send_message(message.chat.id, "Спочатку оберіть звання за допомогою команди /Ranked.")
    elif message.text == "Назад":
        from handlers.ranked import ranked
        ranked(bot, message)
    else:
        bot.send_message(message.chat.id, "Будь ласка, оберіть звання або роль із запропонованих.")
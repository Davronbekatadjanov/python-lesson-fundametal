"""
Mavzu:Kirill-Lotin telegram bot
Sana:09:03:2023
Muallif:Atadjanov Davronbek
telegram:@
"""
from transliterate import to_cyrillic,to_latin

import telebot

TOKEN = '6129938372:AAG114SUApr0jV-EUPM1suPnDgc5NGpZavQ'
bot = telebot.TeleBot(TOKEN, parse_mode=None)

@bot.message_handler(commands=['start'])
def send_welcome(message):
    javob = "Assalom alaykum,Xush kelibsiz!"
    javob += "/Matn kiriting:"
    bot.reply_to(message, javob)
    
@bot.message_handler(func=lambda message: True)
def echo_all(message):
    msg = message.text
    if msg.isascii():
        javob = to_cyrillic(msg)
    else:
        javob = to_latin(msg)
    bot.reply_to(message, javob)
    
bot.infinity_polling()


# matn = input("Matn kiriting>>")--
# if matn.isascii():
#     print(to_cyrillic(matn))
# else:
#     print(to_latin(matn))
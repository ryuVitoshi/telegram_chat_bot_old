from ast import Lambda
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import credentials
import texts
import design

bot = credentials.bot

bot.set_my_commands([
    telebot.types.BotCommand("/start", "Welcome message"),
    telebot.types.BotCommand("/help", "Information about bot")
])

@bot.callback_query_handler(func=lambda message:True)
def button_press_handler(call):
    data = call.data
    uid = call.from_user.id
    print(data)
    print(uid)
    
    if data == 'test':

        pass

    elif data == '':
        pass

# Commands

# Welcome message
start_commands = ["start", "home"]
@bot.message_handler(start_commands)
def send_welcome(message):
    uid = message.from_user.id
    print(uid)
    photo = open('images/welcome.jpg', 'rb')
    #bot.send_photo(uid, photo, texts.WELCOME_TEXT, parse_mode='html', reply_markup = design.welcome_message_with_buttons())
    bot.send_message(uid, photo, texts.KEYBOARD, parse_mode='html', reply_markup = design.keyboard()) 

# HELP message
start_commands = ["help"]
@bot.message_handler(start_commands)
def send_help(message):
    print(message.from_user.id)
    pass


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.polling()
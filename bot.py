from ast import Lambda
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import credentials

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

# Welcoming message
start_commands = ["start", "home"]
@bot.message_handler(start_commands)
def send_welcome(message):
    print(message.from_user.id)
    pass

# HELP message
start_commands = ["help"]
@bot.message_handler(start_commands)
def send_welcome(message):
    print(message.from_user.id)
    pass


bot.enable_save_next_step_handlers(delay=2)

bot.load_next_step_handlers()

bot.polling()
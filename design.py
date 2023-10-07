
from ast import Lambda
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton
import texts
import credentials

bot = credentials.bot

# Key words
start_commands= ["/start","/help", "/home"]
other_commands = ['/profile','/aboutus','/services','/question']
menu_options = ['🚘 services','home', '🌎 about us','👩‍🏫 profile']
menu_hello_options = ['home','hi','hello','start','help','menu','back']
menu_ask_options = ['question','questions','ask','suggestion']
menu_products = ['products','product','service','services']
menu_price_services = ['price', 'prices','cost'] +menu_products
all_keywords = start_commands+ other_commands+menu_options+menu_hello_options+menu_ask_options+menu_price_services


#---------------------BUTTONS LAYOUT DESIGN------------------
# Helper function for building a list of buttons in a grid
def build_menu(buttons, n_cols, header_buttons=None, footer_buttons=None):
    menu = [buttons[i:i + n_cols] for i in range(0, len(buttons), n_cols)]
    if header_buttons:
        menu.insert(0, header_buttons)
    if footer_buttons:
        menu.append(footer_buttons)
    return menu


#--------------------KEYBOARD MENU------------------
# Define keyboard options
def keyboard():
    menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn0 = types.KeyboardButton("Back")
    btn1 = types.KeyboardButton("Home")
    btn2 = types.KeyboardButton("🚘 services")
    btn3 = types.KeyboardButton("🌎 about us")
    btn4 = types.KeyboardButton("👩‍🏫 profile")
    menu_keyboard.add(btn2,btn3,btn4).add(btn0,btn1)
    #🚘  🏠 
    return menu_keyboard


@bot.message_handler(func=lambda message: message.text.lower() in menu_options)
@bot.message_handler(func=lambda message:message.text.lower()=="profile")
@bot.message_handler(func=lambda message:message.text.lower() in menu_hello_options)
def handle_menu_click(message):
    if (message.text.lower() == "home")|(message.text.lower() in menu_hello_options):
        photo = open('imgs/welcome.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo, texts.WELCOME_TEXT,parse_mode='html',reply_markup = welcome_message_with_buttons())
        bot.send_message(message.from_user.id,texts.KEYBOARD,parse_mode='html', reply_markup = keyboard()) 
    elif message.text.lower() == "🌎 about us":
       company_info(message)
    elif (message.text.lower() == '👩‍🏫 profile')|(message.text =="profile"):
        contacts.contacts_msg(message)
    elif (message.text.lower() == '🚘 services'):
        services.pricelist(message)
        bot.send_message(message.from_user.id,"Services options 👇", reply_markup = services.keyboard_services()) 


#-----------------WELCOME BTNS---------
def welcome_message_with_buttons():   
    button_list =  [
        InlineKeyboardButton("Our contacts", callback_data='contacts'),
        InlineKeyboardButton("Services and Products", callback_data='sap'),
        InlineKeyboardButton("Your profile", callback_data='profile')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))
    return reply_markup

#------------------1. COMPANY INFO---------------------------
@bot.message_handler(commands=["aboutus"])
def company_info(message):
    button_list =  [
        InlineKeyboardButton("🌐 Our website", url='https://facebook.com')
    ]
    reply_markup = InlineKeyboardMarkup(build_menu(button_list, n_cols=1))    
    bot.send_message(message.from_user.id,texts.COMPANY_INFO,parse_mode='html',reply_markup=reply_markup)


 
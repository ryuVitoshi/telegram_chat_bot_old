from ast import Lambda
from pickle import TRUE
import telebot
from telebot import types
from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton, Message
import credentials
import design
import sqlite3
import texts
import models

bot = credentials.bot

services_dict = models.services_dict
service_names = ['diagnostics']

def service_info(service_id):
    con = sqlite3.connect("supercar.db")
    c = con.cursor()
    
    c.execute('SELECT * FROM services WHERE service_id=?',(service_id,))
    #services = c.fetchall()
    service = c.fetchone()

    if service:
        service_info = {
            'service_id': service[0],
            'service_name': service[1],
            'service_info': service[2],
            'price': service[3]
        }
        #print(service_info)

        con.close()
        return service_info
    else:
        return None


def services_info(service_name):
    con = sqlite3.connect("supercar.db")
    c = con.cursor()

    c.execute('SELECT * FROM services WHERE service_name=?',(service_name,))
    #services = c.fetchall()    
    service = c.fetchone() 

    if service:        
        service_info = {
            'service_id': service[0],
            'service_name': service[1],
            'service_info': service[2],
            'price': service[3]
        }

        con.close()
        return service_info
    else:
        return None

def service(name):
    service = services_info(name)
    if service!=None:        
        srvc = models.Service(name)
        srvc.name = service['service_name']
        srvc.price = service['price']

        services_dict[name] = srvc
        return srvc
    
    return None

#------------------------------PRICELIST------------------------------
def pricelist(message):
    name = 'undercarriage diagnostics'
    undercarriage_msg = ''
    if (service(name)!=None):
        undercarriage_msg = f"\n   -	Undercarriage diagnostics - <b>BGN {services_dict[name].price}</b>;"

    name = 'computer diagnostics'
    comp_diagnostic_msg = ''
    if (service('computer diagnostics')!=None):
        comp_diagnostic_msg = f"\n   -	Computer diagnostics - <b>BGN {services_dict[name].price}</b>;" #comp_diagnostic['price']

    name = 'maintenance'
    maintenance_msg=''
    if (service('maintenance')!=None):
        maintenance_msg = f"\n   -	Maintenance - <b>from BGN {services_dict[name].price}</b>;"

    name = 'painting'
    painting_msg=''
    if (service(name)!=None):
        painting_msg = f"\n   -	Painting, scaffolding of a car - <b>from BGN {services_dict[name].price}</b>;"

    scaffolding = service('scaffolding')

    name = 'polishing'
    polishing_msg=''
    if (service(name)!=None):
        polishing_msg = f"\n   -	Car polishing - <b>from BGN {services_dict[name].price}</b>."

    for i in services_dict:
       # print(f'{services_dict[i].name} {services_dict[i].price}')
        service_names.append(services_dict[i].name)

    text = f'''🎩 Our company provides a wide range of services. 
You can learn about each in detail by selecting an option in the keyboard!
    
    💸 <b>Price list</b> 💸
{undercarriage_msg}{comp_diagnostic_msg}{maintenance_msg}{painting_msg}{polishing_msg}

❗ <b>Please note that prices may vary depending on the complexity of the work. ✅</b>
'''
    bot.send_message(message.from_user.id,text,parse_mode='html',reply_markup=keyboard_services())

#------------------2.SERVICES---------------------

services_btns = ["🔍Diagnostics","💧Maintenance","💨Conditioner","🌈Painting","🪛Repair","⬅️Back","Ask question❓"]

def keyboard_services():
    menu_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("🔍Diagnostics")
    btn2 = types.KeyboardButton("💧Maintenance")
    btn3 = types.KeyboardButton("💨Conditioner")
    btn5 = types.KeyboardButton("🌈Painting")
    btn6 = types.KeyboardButton("🪛Repair")
    btn_back = types.KeyboardButton("⬅️Back")
    btn_ask = types.KeyboardButton("Ask question❓")

    menu_keyboard.add(btn1,btn2,btn3,btn5,btn6).add(btn_back,btn_ask)
    return menu_keyboard


@bot.message_handler(func=lambda message: message.text in services_btns)
@bot.message_handler(func=lambda message: message.text.lower() in service_names)
def handle_menu_click(message):
    if (message.text =="🔍Diagnostics")|(message.text.lower() =='diagnostics'):
        bot.send_message(message.from_user.id,texts.DIAGNOSTICS, parse_mode='html',reply_markup = diagn_bttns())
    elif message.text == "💧Maintenance":
        maintence(message)  #comments maintence_components
    elif message.text == "💨Conditioner":
        conditioner(message)
    elif message.text == "🌈Painting":
        painting(message)
    elif message.text == "🪛Repair":
        photo = open('imgs/repair.jpg', 'rb')
        bot.send_photo(message.from_user.id,photo,"Sign up for repair", parse_mode='html',reply_markup = signup('repair')) #comments
    elif message.text == "⬅️Back":
        #bot.send_message(message.from_user.id,"How can we help you?", reply_markup = design.keyboard())
        photo = open('imgs/welcome.jpg', 'rb')
        bot.send_photo(message.from_user.id, photo, texts.WELCOME_TEXT,parse_mode='html',reply_markup = design.welcome_message_with_buttons())
        bot.send_message(message.from_user.id,texts.KEYBOARD, parse_mode='html',reply_markup = design.keyboard()) 
    elif message.text == "Ask question❓":
        button_list =  [
        InlineKeyboardButton("Chat with manager", url='https://t.me/ryuVitoshi')
        ]
        reply_markup = InlineKeyboardMarkup(design.build_menu(button_list, n_cols=1))
        photo = open('imgs/question.jpg', 'rb')
        bot.send_photo(message.from_user.id,photo,texts.ASK,parse_mode='html',reply_markup = reply_markup) 


def signup(service_name):
    button_list =  [
        InlineKeyboardButton("Sign up", callback_data=service_name)
    ]
    reply_markup = InlineKeyboardMarkup(design.build_menu(button_list, n_cols=2))
    return reply_markup
#---------------------SERVICES INFO--------------

#DIAGNOSTIC------------------------------
def diagn_bttns():
    button_list =  [
        InlineKeyboardButton("Undercarriage diagnostics",callback_data = "under_diagnostic"),
         InlineKeyboardButton("Computer diagnostics", callback_data = "comp_diagnostic")
    ]
    reply_markup = InlineKeyboardMarkup(design.build_menu(button_list, n_cols=2))
    return reply_markup

def under_diagnostic(chat_id):

    name = 'undercarriage diagnostics'
    if (service(name)!=None):
        photo = open('imgs/under.jpg', 'rb')
        bot.send_photo(chat_id,photo,f'''⚙️<b>Undercarriage diagnostics</b>⚙️
    
✅ We will carry out a qualitative inspection of <b>all components and elements</b> of the chassis that affect safety and quality of driving.
✅ We will also advise on the replacement of auto parts.

💸 Estimated price – <b>BGN {services_dict[name].price}</b>.
    
👍If necessary, we can also <b>order new spare parts or carry out repairs</b>, after agreement with you.
💸 The price of this service depends on the complexity of the work, approximately from <b>BGN {services_dict[name].price+15}</b>.
    
<b>Sign up</b> for undercarriage diagnosis 👇👇👇''',parse_mode='html', reply_markup = signup('undercarriage'))

    else:
        text ="Unfortunetly, service unavailable 😔"
        bot.send_message(chat_id,text,parse_mode='html')


def comp_diagnostic(chat_id):
    name = 'computer diagnostics'
    comp_diagnostic = service(name)
    if comp_diagnostic!=None:
        comp_diagnostic_price = services_dict[name].price
        photo = open('imgs/comp.jpg', 'rb')
        bot.send_photo(chat_id,photo, f'''🖥️<b>Computer diagnostics</b>🖥️

✅ We will check all <b>nodes and control units</b> of your car for the presence of errors that affect the safety and quality of driving.
❗️(The work is performed using <b>the official computer diagnostic software</b> LAUNCH X-431 PRO v4.0)
    
💸 Approximate price – <b>BGN {comp_diagnostic_price}</b>.
    
<b>Sign up</b> for computer diagnostics 👇👇👇''',parse_mode='html',reply_markup = signup('computer'))


#CAR MAINTENCES-------------------------------------
def maintence(message):
    maintenance ='maintenance'
    comprehensive = 'comprehensive maintenance'
    if (service(maintenance)!=None)|(service(comprehensive)!=None):
        maintenance_price = services_dict[maintenance].price
        comprehensive_maintenance_price = services_dict[comprehensive].price

        text = f'''🔩<b>Car maintenance</b>🔩

This section includes the following services:
    1. Changing oil and filtering - <b>from BGN {maintenance_price}</b>.💧
    2. Comprehensive maintenance - <b>from BGN {comprehensive_maintenance_price}</b>.🩸
    (replacement of oil and filters, check of running gear and computer adjustment) 

<b>Sign up</b> for maintenance 👇👇👇'''
        photo = open('imgs/maintenance.jpeg', 'rb')
        bot.send_photo(message.from_user.id,photo, text, parse_mode='html',reply_markup = maintence_types())
    else:
        text ="Unfortunetly, service unavailable 😔"
        bot.send_message(message.from_user.id,text,parse_mode='html')
    

def maintence_types():
    button_list =  [
        InlineKeyboardButton("Maintenance", callback_data='maintenance'),
        InlineKeyboardButton("Comprehensive maintenance", callback_data='comprehensive_maintenance')
    ]
    reply_markup = InlineKeyboardMarkup(design.build_menu(button_list, n_cols=1))
    return reply_markup

def maintence_components(call):
    text =  f'''📃 <b>Availability and ordering of components</b> 📃
    
✅ Indicate if you have oil and filters available (For example: 2 liters of oil, 4 filters).

✍️ Indicate if you need something to order:
    -	Oil 💧
    -	Filter 🛢️
    -	Everything 🗒️'''
    return text
    #bot.send_message(call.from_user.id,text,parse_mode='html')

  #CONDITIONER------------------------------
def conditioner(message):

    name = 'refueling air conditioner'
    if service(name)!=None:
        conditioner_price = services_dict[name].price
        text =  f'''🌀Refueling the air conditioner🌀
    
💸 The price depends on the volume of freon and additional work on system diagnostics.
    
Approximetly <b>BGN {conditioner_price}</b>.
    
    Sign up for a refueling the air conditioner 👇👇👇'''
        photo = open('imgs/conditioner.jpg', 'rb')
        bot.send_photo(message.from_user.id,photo,text, parse_mode='html',reply_markup = signup('conditioner'))
    else:
        text ="Unfortunetly, service unavailable 😔"
        bot.send_message(message.from_user.id,text,parse_mode='html')

#PAINTING------------------------------------
def painting(message):
    pam=''
    sm=''
    pm=''
    paint = 'painting'
    if service(paint)!=None:
        painting_price = services_dict[paint].price
        pam = f"\n    -	Painting of 1 element - from <b>BGN {services_dict[paint].price}</b>;"
        
    scaffolding = 'scaffolding'
    if service(scaffolding)!=None:
        scaffolding_paint_price = services_dict[scaffolding].price+painting_price
        sm = f"\n    -	Scaffolding with painting – <b>from BGN {services_dict[scaffolding].price+painting_price}</b>;"

    polishing = 'polishing'
    if service(polishing)!=None:
        polishing_price = services_dict[polishing].price
        pm = f"\n   -	Polishing - <b>from BGN {polishing_price}</b>."

    if(pam,sm,pm!=''):
        text =  f'''✨Scaffolding, painting, polishing of the car🎨

💸 The price depends on the volume of work and its urgency:
    {pam}{sm}{pm}

<b>Choose</b> the required variant and <b>sign up</b>👇👇👇'''
        photo = open('imgs/painting.jpg', 'rb')
        bot.send_photo(message.from_user.id,photo,text,parse_mode='html',reply_markup = pps_type())
     
    else:
         text ="Unfortunetly, service unavailable 😔"
         bot.send_message(message.from_user.id,text,parse_mode='html')


def pps_type():
    button_list =  [
        InlineKeyboardButton("Painting", callback_data='painting'),
        InlineKeyboardButton("Scaffolding", callback_data='scaffolding'),
        InlineKeyboardButton("Polishing", callback_data='polishing'),
        InlineKeyboardButton("Scaffolding and painting", callback_data='scaffolding_painting'),
        InlineKeyboardButton("Everything", callback_data='p_everything')
    ]
    reply_markup = InlineKeyboardMarkup(design.build_menu(button_list, n_cols=2))
    return reply_markup
#HELP
desc = "This bot was created for online consultation of customers of our car maintance service.\nWith its help, you can view services, as well as make an appointment."
coms = '''
Bot commands:
/start - display welcome message
/help - provides information about bot
/aboutus - information about our comany
/services - provide informtion about our sevices and products 
/profile - your contact information
/question - share with manager your questions and suggestions

You can also press the buttons on the keyboard below. 
There you can find our services, information about us, your profile and a "Home" button that returns you to the initial message.
'''
HOW_HELP='How can we help you?\nPlease, chose an option bellow 👇'
HELP_TEXT= f'Welcome!\n{desc}\n{coms}\n{HOW_HELP}'
KEYBOARD = "Our services, contacts and your profile"

#WELCOME
WELCOME_TEXT='''🚙 Welcome to <b>Super Barbershop!</b> 🚙
'''

# Company info
name = "<b>Super Barbershop</b>"
desc = ""
phone = "+38(012)-345-5678"
email = "superbarbershop@hmail.com"
location = "69000 Zaporizhzhia, Zaporizka street"
owner = "Dimitriy Slaveykov"
COMPANY_INFO = f'{name}\n{desc}\n📍{location}\n✉️ {email}\n📞 {phone} \t{owner}'


# Ask
ASK = '''❓Got questions or suggestions? <b>Share with us</b>!

🗣️Our managers will provide answers at <b>the first opportunity</b>!
🗓️ Business hours are <b>Monday-Friday</b> from <b>9:00 a.m.</b> to <b>6:00 p.m</b>

\nThank you for understanding ✅
'''

#DIAGNOSTIC
DIAGNOSTICS = '''📊 <b>Diagnostics</b> 📊 

Our service carries out two types of car diagnostics. You can learn more about each of them and sign up below 👇'''


import logging
from telegram import ReplyKeyboardMarkup, KeyboardButton
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, ConversationHandler

logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

ADMIN_ID= 0
users={}

def start(update, context):
    reply_text = 'Salom! telefon raqamingizni kiriting:'
    reply_markup = ReplyKeyboardMarkup([
        [KeyboardButton(text="Telefon kontaktinngizni ulashing", request_contact=True)]
    ], resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id, text=reply_text, reply_markup=reply_markup)
    logging.info(f"user - {update.effective_user.id} started")

    return 'PHONE_NUMBER'


def phone_number(update, context):
    phone_number = update.message.contact.phone_number
    context.user_data['phone_number'] = phone_number
    print(context.user_data["phone_number"])
    update.message.reply_text('Rahmat! Ismingiz nima?')
    return 'FIRST_NAME'


def first_name(update, context):
    first_name = update.message.text
    context.user_data['first_name'] = first_name
    update.message.reply_text('Rahmat! Familyangiz nima?')
    return 'LAST_NAME'


def last_name(update, context):
    last_name = update.message.text
    context.user_data['last_name'] = last_name
    update.message.reply_text('Rahmat! yoshingiz?')
    return 'AGE'


def age(update, context):
    age = update.message.text
    context.user_data['age'] = age
    reply_markup = ReplyKeyboardMarkup([
        [KeyboardButton(text="erkak")],[KeyboardButton(text="ayol")]
    ], resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id,
                             text="Jinsingizni tanlang:",
                             reply_markup=reply_markup)

    return 'GENDER'


def gender(update, context):
    gender = update.message.text
    context.user_data['gender'] = gender
    reply_markup = ReplyKeyboardMarkup([
        [KeyboardButton(text="lokatsiyanngizni ulashing", request_location=True)]
    ], resize_keyboard=True, one_time_keyboard=True)
    context.bot.send_message(chat_id=update.effective_user.id, text="lokatsiyanngizni ulashing:", reply_markup=reply_markup)
    return 'GEOLOCATION'


def geolocation(update, context):
    latitude = update.message.location.latitude
    longitude = update.message.location.longitude
    context.user_data['latitude'] = latitude
    context.user_data['longitude'] = longitude
    users["Phone_nuber"]=context.user_data['phone_number']
    users["First_name"]=context.user_data['first_name']
    users["last_name"]=context.user_data['last_name']
    users['Age']=context.user_data['age']
    users["Gender"]=context.user_data['gender']
    users["Latitude"]=context.user_data['latitude']
    users["Longitude"]=context.user_data['longitude'],
    print(users)
    logging.info("User Registered")
    update.message.reply_text(f"Rahmat, {users['First_name'] }\n    to'liq ro'yxatdan o'tdingiz !!!")
    context.bot.send_message(chat_id=ADMIN_ID,text=F"""
    Telfon : {users["Phone_nuber"]}
    Ism : {users['First_name']}
    Familiya : {users['last_name']}
    Yosh : {users['Age']}
    Jinsi : {users["Gender"]}
    
    
    
    """)
    return ConversationHandler.END


def cancel(update, context):
    update.message.reply_text(text='Bekor qilindi!')
    return ConversationHandler.END


def main():
    updater = Updater(token="#")
    dispatcher = updater.dispatcher

    conv_handler = ConversationHandler(
        entry_points=[CommandHandler('start', start)],

        states={
            'PHONE_NUMBER': [MessageHandler(Filters.contact & ~Filters.command, phone_number)],
            'FIRST_NAME': [MessageHandler(Filters.text & ~Filters.command, first_name)],
            'LAST_NAME': [MessageHandler(Filters.text & ~Filters.command, last_name)],
            'AGE': [MessageHandler(Filters.text & ~Filters.command, age)],
            'GENDER': [MessageHandler(Filters.text & ~Filters.command, gender)],
            'GEOLOCATION': [MessageHandler(Filters.location & ~Filters.command, geolocation)],

        },
        fallbacks=[CommandHandler('cancel', cancel)]
    )
    dispatcher.add_handler(conv_handler)
    updater.start_polling()


if __name__ == '__main__':
    main()

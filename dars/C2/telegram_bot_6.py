token="#"
ADMIN_ID=0
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton
from geo_name import geo_location_name

def start_func(update, context):
    update.message.reply_text(text="Salom xush kelibsiz!!!")
    update.message.reply_text(text="/menu")

def show_menu(update,context):
    buttons=[

        [KeyboardButton(text="Send Contact",request_contact=True),
        KeyboardButton(text="Send Location",request_location=True),

         ],
        [
            KeyboardButton(text='Send Audio'),
            KeyboardButton(text="Send Photo")
        ],
    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    )
def message_func(update,context):
    xabar=update.message.text
    if xabar=='Send Photo':
        update.message.reply_photo(photo="https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg")
    elif xabar=="Send Audio":
        update.message.reply_audio(audio="https://muzbass.com/uploads/files/2024-04/Xamdam-Sobirov-Malohat-2_(muzbass_com).mp3")
    else:
        update.message.reply_text(text=f"Sizning xabaringiz ==>> {xabar}")

def contact_func(update,context):
    phone_number=update.message.contact.phone_number
    # update.message.reply_text(text=f"Sizning nomeringiz ==>>{phone_number}")
    context.bot.send_message(chat_id=ADMIN_ID,text=f"Yangi foydalanuvchi raqami ===>>>{phone_number}")
def location_func(update,context):
    location=update.message.location
    update.message.reply_text(text="Yangi foydalanuvchi manzili.")
    address=geo_location_name(location.latitude,location.longitude)
    print(address)
    list_address=address.split(",")
    update.message.reply_text(text=f"""Davlat : {list_address[-1]}
    Pochta raqam : {list_address[-2]}
    Viloyat : {list_address[-3]}
    Tuman : {list_address[-4]}
    Shahar/Qishliq : {list_address[-5]}
    
    """)

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text,message_func))
    dispatcher.add_handler(MessageHandler(Filters.contact,contact_func))
    dispatcher.add_handler(MessageHandler(Filters.location,location_func))



    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
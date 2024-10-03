token="7408760828:AAEKrKsMOHVLIIocJoN3Y8uubfFPAXWsLIo"
ADMIN_ID=6317196964
from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton


def start_func(update, context):
    update.message.reply_text(text="Salom xush kelibsiz!!!")
    update.message.reply_text(text="/menu")

def show_menu(update,context):
    buttons=[

        [KeyboardButton(text="Send Number",request_contact=True),
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
        # update.message.reply_photo(photo=open('112.png','r'))
        # chat_id = update.effective_chat.id
        # # Rasimni joylashgan manzilini bu yerga kiriting, masalan:
        # photo_path = 'path/to/your/image.jpg'
        # # Rasimni yuborish
        # context.bot.send_photo(chat_id=chat_id, photo=open(photo_path, 'rb'))
        update.message.reply_text(text=open("112.png",'rb'))



    elif xabar=="Send Audio":
        update.message.reply_audio(audio="https://muzbass.com/uploads/files/2024-04/Xamdam-Sobirov-Malohat-2_(muzbass_com).mp3")
    else:
        update.message.reply_text(text=f"Sizning xabaringiz ==>> {xabar}")

def contact_func(update,context):
    phone_number=update.message.contact.phone_number
    update.message.reply_text(text=f"Sizning nomeringiz ==>>{phone_number}")
    context.bot.send_message(chat_id=ADMIN_ID,text=f"Yangi foydalanuvchi raqami ===>>>{phone_number}")
def location_func(update,context):
    location=update.message.location
    update.message.reply_text(text="Yangi foydalanuvchi manzili.")
    # update.message.reply_location(latitude=location.latitude,longitude=location.longitude)
    context.bot.send_location(chat_id=ADMIN_ID,latitude=location.latitude,longitude=location.longitude)
    print(location.latitude,location.longitude)

def main():
    updater = Updater(token=token,use_context=True)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text,message_func))
    dispatcher.add_handler(MessageHandler(Filters.contact,contact_func))
    dispatcher.add_handler(MessageHandler(Filters.location,location_func))



    updater.start_polling()
    updater.idle()

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
token="7393833956:AAGJvaWDD5l9i-rsWP8BTHOu8pDrZSz_6KY"

def start_func(update, context):
    update.message.reply_text(text="Salom xush kelibsiz!!!")
    update.message.reply_text(text="      /photo\n   /audio\n    /vedio")

# def show_menu(update,context):
#     buttons=[
#         [KeyboardButton(text="photo"),
#         KeyboardButton(text="Send Vedio")],
#     ]
#     update.message.reply_text(
#         text="Menu",
#         reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=True)
#     )

def photo_func(update,context):
    update.message.reply_photo(photo="https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg")
    update.message.reply_text(text="    /photo\n   /audio\n    /vedio")


def vedio_func(update,context):
    update.message.reply_text(text="https://youtu.be/b3qNwcVrP5k")
    update.message.reply_text(text="    /photo\n   /audio\n    /vedio")

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(CommandHandler("photo",photo_func))
    dispatcher.add_handler(CommandHandler("vedio",vedio_func))
    # dispatcher.add_handler(CommandHandler('menu', show_menu))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
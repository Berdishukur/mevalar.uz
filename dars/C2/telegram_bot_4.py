token="7393833956:AAGJvaWDD5l9i-rsWP8BTHOu8pDrZSz_6KY"

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton


def start_func(update, context):
    update.message.reply_text(text="Salom xush kelibsiz!!!")
    update.message.reply_text(text="/menu")

def show_menu(update,context):
    buttons=[

        [KeyboardButton(text="Send Contact"),
        KeyboardButton(text="Send Location"),

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
    else:
        update.message.reply_text(text=f"Sizning xabaringiz ==>> {xabar}")


def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(CommandHandler('menu', show_menu))
    dispatcher.add_handler(MessageHandler(Filters.text,message_func))



    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
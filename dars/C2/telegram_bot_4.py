token="7393833956:AAGJvaWDD5l9i-rsWP8BTHOu8pDrZSz_6KY"

from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
from telegram import ReplyKeyboardMarkup,KeyboardButton


def start_func(update, context):
    update.message.reply_text(text="Salom xush kelibsiz!!!")
    update.message.reply_text(text="/menu")

def show_menu(update,context):
    buttons=[

        [KeyboardButton(text="Send Photo"),
        KeyboardButton(text="Send Vedio"),

         ],
        [
            KeyboardButton(text='Send Audio'),
            KeyboardButton(text="Send Contact")
        ],
    ]
    update.message.reply_text(
        text="Menu",
        reply_markup=ReplyKeyboardMarkup(buttons, resize_keyboard=True, one_time_keyboard=False)
    )

def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_func))

    dispatcher.add_handler(CommandHandler('menu', show_menu))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
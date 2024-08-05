from telegram.ext import Updater,CommandHandler,MessageHandler,Filters
token="7393833956:AAGJvaWDD5l9i-rsWP8BTHOu8pDrZSz_6KY"

def start_func(update, context):
    update.message.reply_text(text="Salom xush kelibsiz!!!")
def photo_func(update,context):
    update.message.reply_photo(photo="https://images.pexels.com/photos/45201/kitty-cat-kitten-pet-45201.jpeg")

def message_func(update,context):
    xabar=update.message.text
    if xabar.lower()=="salom":
        update.message.reply_text(text="Valaykum assalaom.")
    elif xabar.lower()=="qalaysiz":
        update.message.reply_text(text="Men yaxshiman \n  O'zingiz ham yaxshimisiz?")
    else:
        update.message.reply_text(text="Menu ni tanlang\n   \n /photo \n /Audio")



def main():
    updater = Updater(token=token)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('start', start_func))
    dispatcher.add_handler(CommandHandler("photo",photo_func))
    dispatcher.add_handler(MessageHandler(Filters.text,message_func))


    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
import os
from telegram.ext import Updater, CommandHandler

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="Hello!")

def main():
    TOKEN = os.environ.get('TOKEN')
    with Updater(TOKEN, use_context=True) as updater:
        dp = updater.dispatcher
        dp.add_handler(CommandHandler('start', start))
        updater.start_polling()
        updater.idle()

if __name__ == '__main__':
    main()

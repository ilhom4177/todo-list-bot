from telegram.ext import Updater, CommandHandler
from todo import (
    start,
)
import os

TOKEN = os.environ.get('TOKEN')


def main():
    # updater obj
    updater = Updater(token=TOKEN)

    # dispetcher obj
    dp = updater.dispatcher

    # handlers
    dp.add_handler(CommandHandler(['start', 'boshlash'], start))


    # polling started
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackQueryHandler
from todo import (
    start,
    get_tasks,
    add_task,
    delete_task,
    mark,
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
    dp.add_handler(MessageHandler(Filters.text('my tasks'), get_tasks))
    dp.add_handler(MessageHandler(Filters.text, add_task))
    dp.add_handler(CallbackQueryHandler(callback=delete_task, pattern=('delete_task')))
    dp.add_handler(CallbackQueryHandler(callback=mark, pattern=('mark')))

    # polling started
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
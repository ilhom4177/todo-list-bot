from telegram import Update
from telegram.ext import CallbackContext


def start(update: Update, context: CallbackContext):
    '''start function'''
    update.message.reply_markdown_v2('*Hello, welcome to our bot\!*')
    

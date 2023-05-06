import requests
from .settings import base_url
from telegram import Update
from telegram.ext import CallbackContext



def start(update: Update, context: CallbackContext):
    '''start function'''
    chat_id = update.message.chat.id
    first_name = update.message.chat.first_name
    user = {
        'chat_id': chat_id,
        'first_name': first_name
    }
    username = update.message.chat.username
    if username is not None: user['username'] = username
    last_name = update.message.chat.last_name
    if last_name is not None: user['last_name'] = last_name

    url_for_register = f'{base_url}/create-user'
    response = requests.post(url_for_register, json=user)


    update.message.reply_markdown_v2('*Hello, welcome to our bot\!*')
    

def get_tasks(update: Update, context: CallbackContext):
    '''add new task'''
    pass
    

def add_task(update: Update, context: CallbackContext):
    '''add new task'''
    pass
    

def delete_task(update: Update, context: CallbackContext):
    '''add new task'''
    pass
    

def mark(update: Update, context: CallbackContext):
    '''add new task'''
    pass


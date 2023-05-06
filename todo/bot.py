import requests
from .settings import base_url
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton
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

    btn = KeyboardButton(text='my tasks')
    update.message.reply_markdown_v2(
        '*Hello, welcome to our bot\!*\n\n_select name for creating task_',
        reply_markup=ReplyKeyboardMarkup(keyboard=[[btn]]))
    

def get_tasks(update: Update, context: CallbackContext):
    '''add new task'''
    pass
    

def add_task(update: Update, context: CallbackContext):
    '''add new task'''
    text = update.message.text
    chat_id = update.message.chat.id

    url_for_add_task = f'{base_url}//create-task/{chat_id}'
    data = {
        "name": text
    }
    response = requests.post(url_for_add_task, json=data)
    print(response.status_code)
    update.message.reply_markdown_v2('*added task*')
    

def delete_task(update: Update, context: CallbackContext):
    '''add new task'''
    pass
    

def mark(update: Update, context: CallbackContext):
    '''add new task'''
    pass


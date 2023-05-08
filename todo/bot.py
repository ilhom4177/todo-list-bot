import requests
from .settings import base_url
from telegram import Update, ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton
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
    chat_id = update.message.chat.id

    url_for_get_tasks = f'{base_url}/get-tasks/{chat_id}'
    response = requests.get(url_for_get_tasks)

    msg = ''
    if response.status_code == 200:
        tasks = response.json()
        
        for task in tasks:
            btn = InlineKeyboardButton(text=task['name'], callback_data=task['name'])
            if task['done']:
                msg += f'✅ {task["name"]}\n'
            else:
                msg += f'❌ {task["name"]}\n'
    update.message.reply_html(msg)
    

def add_task(update: Update, context: CallbackContext):
    '''add new task'''
    text = update.message.text
    chat_id = update.message.chat.id

    url_for_add_task = f'{base_url}/create-task/{chat_id}'
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


from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import CommandHandler, MessageHandler, Updater, CallbackContext
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

bot_token = os.getenv("BOT_TOKEN")
updater = Updater(token=bot_token, use_context=True)
dispatcher = updater.dispatcher

@app.route(f'/webhook/{bot_token}', methods=['POST'])
def webhook():
    json_str = request.get_data().decode('UTF-8')
    update = Update.de_json(json_str, updater.bot)
    updater.dispatcher.process_new_updates([update])
    return 'OK'

@app.route('/')
def index():
    return 'Hello, World! This is your Flask app with a Telegram bot.'

def start(update, CallbackContext):
    update.message.reply_text("Hello! I am your Telegram bot.")

def echo(update, CallbackContext):
    update.message.reply_text(update.message.text)

# Use MessageHandler for text messages
text_message_handler = MessageHandler(Filters.text & ~Filters.command, echo)
dispatcher.add_handler(text_message_handler)

# Use CommandHandler for /start command
start_command_handler = CommandHandler('start', start)
dispatcher.add_handler(start_command_handler)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
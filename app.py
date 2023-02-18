from flask import Flask, request
from telegram import Bot, Update
from telegram.ext import Dispatcher, CommandHandler, MessageHandler, Filters
import os


from bot_main import start, echo


TOKEN = os.environ["TOKEN"]

bot = Bot(TOKEN)

app = Flask(__name__)


@app.route('/webhook', methods=["POST", "GET"])
def hello():
    if request.method == 'GET':
        return 'hi from Python2022I'
    elif request.method == "POST":
        data = request.get_json(force = True)
        
        dispacher: Dispatcher = Dispatcher(bot, None, workers=0)
        update:Update = Update.de_json(data, bot)
    
        #update 
        dispacher.add_handler(CommandHandler('start', callback=start))
        dispacher.add_handler(MessageHandler(Filters.text, echo))
        
        dispacher.process_update(update)
        return 'ok'

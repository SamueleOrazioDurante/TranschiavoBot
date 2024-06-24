
import telebot # telegram bot manager

# general utilities
import requests

# script
import tokenManager
import logger
import browser

BOT_TOKEN = tokenManager.read_bot_token()
CHAT_ID = tokenManager.read_chat_id()

bot = telebot.TeleBot(BOT_TOKEN) # instance bot

### extra config for using local telegram API

# bot.logout() # to log out from telegram base API (only first time)

#apihelper.API_URL = 'http://0.0.0.0:6969/bot{0}/{1}'
#apihelper.FILE_URL = 'http://0.0.0.0:6969'

# wetransfer downloader

DOWNLOAD_DIRECTORY = "/usr/src/app/downloads" # default Dockerfile directory

@bot.message_handler(regexp="https://we.tl/") # es https://we.tl/t-9f4P4Jl00w
def wetransfer_dl(message):

    logger.log("Richista download",message)

    if str(message.chat.id) == str(CHAT_ID):
        url = message.text

        # get download url page
        r = requests.get(url) 
        url = r.url
        
        logger.toConsole("Inizio download...")
        
        text = "Download completato con successo! \nPercorso di download (docker): "+browser.WTDownload(url,DOWNLOAD_DIRECTORY)
        logger.toConsole(text)

        bot.send_message(message.chat.id,text)
    else:
        logger.log("Accesso non autorizzato!",message)
        bot.send_message(message.chat.id,"Non sei autorizzato ad utilizzare questo bot!!")


logger.toConsole("---------------------------------------------------")
logger.toConsole("Bot started!")

bot.polling() # bot start

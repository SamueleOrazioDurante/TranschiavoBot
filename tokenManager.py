import os

def read_bot_token():

    #read bot token from config.py file
    BOT_TOKEN = None

    try:
        from config import BOT_TOKEN
    except:
        pass

    if len(BOT_TOKEN) == 0:
        BOT_TOKEN = os.environ.get('BOT_TOKEN')

    if BOT_TOKEN is None:
        raise ('Token for the bot must be provided (BOT_TOKEN variable)')
    return BOT_TOKEN

def read_chat_id():

    #read chat id from config.py file
    CHAT_ID = None

    try:
        from config import CHAT_ID
    except:
        pass

    if len(CHAT_ID) == 0:
        CHAT_ID = os.environ.get('CHAT_ID')

    if CHAT_ID is None:
        raise ('Token for the bot must be provided (CHAT_ID variable)')
    return CHAT_ID
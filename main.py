from Plugins.starter import start
from Plugins.nhentai import Nhentai
from config import bot

try:
    start()
    Nhentai()
    
except Exception as e:
    print(e)

bot.start()

bot.run_until_disconnected()

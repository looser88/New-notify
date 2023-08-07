import aiohttp
from pyrogram import Client, filters
#from config import *

try:
    bot = Client('shortener bot',
                 api_id=int(20259272),
                 api_hash='1fabcb35e58a28a29b575b590160aec5',
                 bot_token=',5951544679:AAEE5qPN1E257bSbRZ1NAIAOMyzSxOUoUac'
                 workers=50,
                 sleep_threshold=10)
except Exception:
    print("Add var values properly. Read readme.md once")


@bot.on_message(filters.command('start'))
async def start(bot, message):
    start_msg = f"""
Hi {message.chat.first_name}!

I'm notify bot. Just send me link and get short link!

Send me a link to short a link with random alias.

    """
    await message.reply_photo(photo='https://graph.org/file/20eee5ed9538ad443e758.jpg', caption=start_msg)





bot.run()

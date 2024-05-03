from aiogram import Bot,Dispatcher,F
from aiogram.types import Message
import asyncio
import logging

import backend

token = '7097427541:AAHw6BzeEZFjqOq4jQYLLybCut-_3MrL4sM'
admin_id='1346629196'

async def bot_started(bot:Bot):
    await bot.send_message(chat_id=admin_id,text = 'bot started')
    # await bot.send_message(chat_id=operator, text='bot started')
async def bot_closed(bot:Bot):
    await bot.send_message(chat_id=admin_id,text = 'bot closed')
    # await bot.send_message(chat_id=operator, text='bot closed')




async def start():
    logging.basicConfig(level=logging.INFO)
    bot = Bot(token=token, parse_mode='HTML')
    dp = Dispatcher()
    # dp.message.register(main_menu,F.text == '/menu')
    
    dp.startup.register(bot_started)
    dp.shutdown.register(bot_closed)

    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == '__main__':
    asyncio.run(start())

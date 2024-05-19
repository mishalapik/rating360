import asyncio
import logging

from aiogram import Dispatcher

from bot_instance import bot
from handlers.user_handlers import user_router



def register_routers(dp: Dispatcher) -> None:
    """Register routers"""
    
    dp.include_router(user_router)


async def main() -> None:
    """The main function to start polling the bot"""
    
    logging.basicConfig(level=logging.INFO)

    dp = Dispatcher()

    register_routers(dp)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    asyncio.run(main())

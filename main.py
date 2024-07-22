import logging
import asyncio

from aiogram import Bot, Dispatcher, F
from aiogram.fsm.storage.memory import MemoryStorage
from TOKEN import API_TOKEN
from handlers import main_handlers


async def main():
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(name)s - %(message)s",
    )

    dp = Dispatcher(storage=MemoryStorage())
    bot = Bot(token=API_TOKEN)

    dp.include_router(main_handlers.router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())

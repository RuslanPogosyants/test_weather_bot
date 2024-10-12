import logging
import os
from aiogram import Bot, Dispatcher
from aiogram.fsm.storage.memory import MemoryStorage
from aiogram.types import BotCommand
from bot.handlers import register_handlers
from bot.database import init_db

API_TOKEN = os.getenv('BOT_API_TOKEN')

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def set_commands(bot: Bot):
    commands = [
        BotCommand(command="/start", description="Запустить бота"),
        BotCommand(command="/help", description="Помощь"),
    ]
    await bot.set_my_commands(commands)


async def main():
    bot = Bot(token=API_TOKEN)
    dp = Dispatcher(storage=MemoryStorage())

    register_handlers(dp)

    init_db()

    await set_commands(bot)

    await dp.start_polling(bot)

if __name__ == '__main__':
    import asyncio
    asyncio.run(main())

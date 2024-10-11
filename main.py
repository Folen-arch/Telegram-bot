import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
import os

from app.handlers import router

# Загружаем переменные окружения из .env файла
load_dotenv()

async def main():
    bot = Bot(token=os.getenv('TELEGRAM_BOT_TOKEN'))  # Получаем токен из переменных окружения
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')

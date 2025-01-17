import asyncio
from aiogram import Bot, Dispatcher

from app import handlers as hls

bot = Bot(token="7761098053:AAG1JEWlOsrH0GTuVv8OLxT98o5oaTK8nOQ")

async def run():
    dp = Dispatcher()
    dp.include_router(hls.router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(run())
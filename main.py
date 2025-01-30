import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router
from app.database.models import async_main


async def main():
    await async_main() # Чтобы при запуске бота создавались все таблицы
    bot = Bot(token='7888407027:AAE9llWgbCSt-cUxwxW9_CeU8-pBAnd8F4A')
    dp = Dispatcher() # Диспетчер обработчик событий
    dp.include_router(router) # Подключить роуты
    await dp.start_polling(bot)


if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Бот выключен')
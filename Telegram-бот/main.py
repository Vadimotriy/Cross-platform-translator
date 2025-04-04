import asyncio

from bot import bot, dp
from handlers import router, router_for_translate

if __name__ == '__main__':  # запуск программы
    dp.include_router(router)
    dp.include_router(router_for_translate)


    async def main():
        await bot.delete_webhook(drop_pending_updates=True)
        await dp.start_polling(bot)


    asyncio.run(main())

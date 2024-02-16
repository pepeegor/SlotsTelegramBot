import asyncio

from aiogram import Bot, Dispatcher

from bot.callbacks import handler
from bot.data.config import TELEGRAM_API_TOKEN
from bot.handlers import user_commands
from bot.handlers import bot_messages
from bot.middlewares.antiflood import AntiFloodMiddleware


async def main():
    bot = Bot(TELEGRAM_API_TOKEN, parse_mode="HTML")
    dp = Dispatcher()

    dp.message.middleware(AntiFloodMiddleware())

    dp.include_routers(
        user_commands.router,
        handler.router,
        bot_messages.router
    )

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())

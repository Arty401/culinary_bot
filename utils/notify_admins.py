import logging

from aiogram import Dispatcher

from data.config import admins


async def notify_admins_on_startup(dp: Dispatcher):
    try:
        for admin in admins:
            await dp.bot.send_message(admin, "Бот успешно запущен")
    except Exception as e:
        logging.exception(e)

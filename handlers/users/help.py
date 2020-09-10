from aiogram import types
from aiogram.dispatcher.filters import CommandHelp

from keyboards.default import menu
from loader import dp


@dp.message_handler(CommandHelp())
async def help_message(message: types.Message):
    await message.answer("Вот все доступные комманды бота:", reply_markup=menu)

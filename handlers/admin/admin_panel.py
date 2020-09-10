from aiogram import types
from aiogram.dispatcher.filters import Command

from filters import IsAdmin
from keyboards.admin import admin_menu
from loader import dp


@dp.message_handler(IsAdmin(), Command('admin', prefixes='!'))
async def show_admin_menu(message: types.Message):
    await message.answer("Вот Ваша панель, мой Бог!", reply_markup=admin_menu)

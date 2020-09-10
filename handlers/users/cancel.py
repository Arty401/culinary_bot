from aiogram import types

from keyboards.default import menu
from loader import dp


@dp.message_handler(text='❌Отмена❌')
async def cancel_menu(message: types.Message):
    await message.answer("Возвращаюсь...", reply_markup=menu)

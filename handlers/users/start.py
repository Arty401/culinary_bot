from aiogram import types
from aiogram.dispatcher.filters import CommandStart

from keyboards.default import menu
from loader import dp


@dp.message_handler(CommandStart())
async def start_message(message: types.Message):
    await message.answer('Приветсвую Вас в кулинарном боте!\n'
                         'Создатель бота - @Arty401\n', reply_markup=menu)

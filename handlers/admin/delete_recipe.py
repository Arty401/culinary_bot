from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsAdmin
from keyboards.admin import admin_menu
from keyboards.default import cancel
from loader import dp, db
from states import DeleteRecipe


@dp.message_handler(IsAdmin(), text='Удалить репецт по названию')
async def delete_recipe_step1(message: types.Message):
    await message.answer("Введите название рецепта: ", reply_markup=cancel)

    await DeleteRecipe.title.set()


@dp.message_handler(IsAdmin(), state=DeleteRecipe.title)
async def delete_recipe_step2(message: types.Message, state: FSMContext):
    title = message.text
    await state.finish()
    if title == "Отмена":
        await message.answer('Ваше меню, Бог!', reply_markup=admin_menu)
        return

    db.delete_recipe(title)

    await message.answer(f"Рецепт с названием \"{title}\" была удалена", reply_markup=admin_menu)

from aiogram import types
from aiogram.dispatcher import FSMContext

from filters import IsAdmin
from keyboards.admin import admin_menu
from loader import dp, db
from states.add_recipe import AddRecipe


@dp.message_handler(IsAdmin(), text='Добавить рецепт')
async def add_recipe_start(message: types.Message):
    await message.answer("Введите название рецепта:")

    await AddRecipe.title.set()


@dp.message_handler(IsAdmin(), state=AddRecipe.title)
async def add_recipe_title(message: types.Message, state: FSMContext):
    title = message.text

    async with state.proxy() as data:
        data['title'] = title

    await message.answer("Введите рецепт:")
    await AddRecipe.recipe.set()


@dp.message_handler(IsAdmin(), state=AddRecipe.recipe)
async def add_recipe_recipe(message: types.Message, state: FSMContext):
    recipe = message.text

    async with state.proxy() as data:
        data['recipe'] = recipe

    await message.answer("Введите ингридиенты через запятую:")
    await AddRecipe.ingredients.set()


@dp.message_handler(IsAdmin(), state=AddRecipe.ingredients)
async def add_recipe_end(message: types.Message, state: FSMContext):
    ingredients = message.text

    async with state.proxy() as data:
        db.add_recipe(data.get('title'), data.get('recipe'), ingredients)

    await state.finish()

    await message.answer(f"Рецепт создан!", reply_markup=admin_menu)

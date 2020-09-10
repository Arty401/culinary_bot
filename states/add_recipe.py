from aiogram.dispatcher.filters.state import StatesGroup, State


class AddRecipe(StatesGroup):
    title = State()
    recipe = State()
    ingredients = State()

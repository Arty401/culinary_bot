from aiogram.dispatcher.filters.state import StatesGroup, State


class SearchByIngredients(StatesGroup):
    ingredients = State()

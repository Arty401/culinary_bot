from aiogram.dispatcher.filters.state import StatesGroup, State


class DeleteRecipe(StatesGroup):
    title = State()

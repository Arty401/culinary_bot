from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

admin_menu = ReplyKeyboardMarkup(
    [
        [KeyboardButton('Добавить рецепт'), KeyboardButton('Удалить репецт по названию')]
    ],
    resize_keyboard=True
)

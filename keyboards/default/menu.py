from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton(text='Все рецепты')
        ],
        [
            KeyboardButton(text='Поиск по названию'),
            KeyboardButton(text='Поиск по ингридиентам')
        ]
    ],
    resize_keyboard=True
)

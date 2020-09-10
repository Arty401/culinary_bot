from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

cancel = ReplyKeyboardMarkup(
    [
        [
            KeyboardButton("❌Отмена❌")
        ]
    ],
    resize_keyboard=True
)

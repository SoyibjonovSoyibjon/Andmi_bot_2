from aiogram.types import (
    InlineKeyboardButton,
    InlineKeyboardMarkup,
    KeyboardButton,
    ReplyKeyboardMarkup,
)

variant_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="A"),
            KeyboardButton(text="B"),
            KeyboardButton(text="C"),
            KeyboardButton(text="D"),
        ]
    ],
    resize_keyboard=True,
    input_field_placeholder="Kerakli variantni tanlang !"
)

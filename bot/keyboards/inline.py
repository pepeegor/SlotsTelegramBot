from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

main = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Продолжить", callback_data='continue')
        ]
    ]
)

user = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Изменить", callback_data="change_username"),
            InlineKeyboardButton(text="Продолжить", callback_data="username_cont")
        ]
    ]
)

slot = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Изменить", callback_data="change_slot"),
            InlineKeyboardButton(text="Продолжить", callback_data="slot_cont")
        ]
    ]
)



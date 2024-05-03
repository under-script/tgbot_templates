from itertools import chain

from aiogram.types.inline_keyboard_button import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


def book_keys_keyboard():
    keyboard = InlineKeyboardBuilder()
    # buttons = [
    #     ["📍 Eng yaqin do'konni topish", "mylocation"],
    #     ["📱 Kontakt ulashish", "mycontact"],
    # ]
    # keyboard.row(*[InlineKeyboardButton(text=i[0], callback_data=i[1]) for i in chain(buttons)], width=1)
    keyboard.add(InlineKeyboardButton(
        text="📍 Eng yaqin do'konni topish",
        callback_data="mylocation",
        request_location=True
    ))
    keyboard.add(InlineKeyboardButton(
        text="📱 Kontakt ulashish",
        callback_data="mycontact",
        request_contact=True
    ))
    return keyboard.as_markup()

from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message

from tgbot.keyboards.inline import book_keys_keyboard

media_router = Router()


@media_router.message(Command("kitob"))
async def send_book(message: Message):
    photo = "https://telegra.ph/file/fd053ddb8d0fbee95e85e.png"
    msg = "<b>Pythonda Dasturlash Asoslari</b> kitobi.\n"
    msg += "Narxi: 50000 so'm\n\n"
    msg += "<b>Kitob quyidagi do'konlarda sotiladi:</b>\n👉Akademnashr\n👉Hilol nashr\n👉Azon kitoblar\n👉Kitoblar dunyosi"
    await message.reply_photo(photo, caption=msg, reply_markup=book_keys_keyboard())

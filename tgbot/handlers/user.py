from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

user_router = Router()


@user_router.message(CommandStart())
async def user_start(message: Message):
    await message.reply("Assalomu alaykum, foydalanuvchi!", reply_markup=ReplyKeyboardRemove())

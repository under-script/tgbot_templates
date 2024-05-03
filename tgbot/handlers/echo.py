from aiogram import types, Router

echo_router = Router()


@echo_router.message()
async def bot_echo(message: types.Message):
    await message.reply("Echo message")

from aiogram import Bot
from aiogram.types import BotCommand, BotCommandScopeDefault


async def set_commands(bot: Bot):
    commands_list = [
        ["start", "Botni ishga tushurish"],
        ["help", "Yordam"],
        ["info"],
        ["info_html"],
        ["info_markdown"],
    ]
    commands = [
        BotCommand(
            command=command[0],
            description=command[1] if len(command) == 2 else command[0],
        ) for command in commands_list
    ]

    await bot.set_my_commands(commands=commands, scope=BotCommandScopeDefault())

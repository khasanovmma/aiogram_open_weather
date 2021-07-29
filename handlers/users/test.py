from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandHelp

from data.config import ADMINS
from loader import dp


@dp.message_handler(CommandHelp())
async def bot_help(message: types.Message):
    if message.chat.id == ADMINS:
        text = 'Bot ishlavotdi❗️❗️❗️'
    else:
        text = 'Uzur siz admin emassiz❗️❗️❗️'

    await message.answer()

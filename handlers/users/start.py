from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from keyboards.default import menu
from loader import dp


@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Salom,  <b>Assalomu aleykum</b>\n\n'
                         f'Ob havoni bilish uchun tugmani bosing.', reply_markup=menu)

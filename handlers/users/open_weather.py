from datetime import datetime, timedelta

from aiogram import types
from aiogram.dispatcher import FSMContext
from pip._vendor import requests

from loader import dp
from states.answer import Answer

from data.config import OPEN_WEATHER_KEY


@dp.message_handler(state=None)
async def get_weather(message: types.Message, state: None):
    if message.chat.type == 'private':
        if message.text == 'Ob havoni bilish':
            await message.reply('Shaharni kiriting:')
            await Answer.user.set()
        else:
            await message.reply('Tugmani bosing❗️❗️❗️')


@dp.message_handler(state=Answer.user)
async def send_weather(message: types.Message, state: FSMContext):
    try:
        r = requests.get(
            f'http://api.openweathermap.org/data/2.5/weather?q={message.text}&appid={OPEN_WEATHER_KEY}&units=metric')
        data = r.json()

        temp = data['main']['temp']
        humidity = data['main']['humidity']
        pressure = data['main']['pressure']
        wind = data['wind']['speed']
        timezone = str(data['timezone'] / 3600).split('.')

        time_now = datetime.now() + timedelta(hours=int(timezone[0]), minutes=int(timezone[1]))

        sunrise_time = datetime.fromtimestamp(data['sys']['sunrise']) + timedelta(hours=int(timezone[0]),
                                                                                  minutes=int(timezone[1]))

        sunset_time = datetime.fromtimestamp(data['sys']['sunset']) + timedelta(hours=int(timezone[0]),
                                                                                minutes=int(timezone[1]))

        await message.answer(f'Bugun <b>{time_now.strftime(" | %d.%m.%Y | %X")}</b> vaqti bilan,\n\n'
                             f'<b>{message.text.title()}dagi ob havo:</b>\n\n'
                             f'Harorat 🌡: {temp} ℃.\n'
                             f'Namlik: {humidity}%.\n'
                             f'Bosim: {pressure} mm sim. ust.\n'
                             f'Shamol 💨: {wind} m/s.\n'
                             f'Quyosh chiqishi 🌄: {sunrise_time.strftime("%H:%M")}.\n'
                             f'Quyosh botishi 🌅: {sunset_time.strftime("%H:%M")}.')
        await state.reset_state()
        await message.answer('Ob havoni bilish uchun tugmani bosing.')

    except Exception as ex:
        print(ex)
        await message.reply(f'<b>Shahar nomi noto\'g\'ri kiritildi❗️❗️❗️</b>\n\n'
                            f'Qaytatdan kiriting:')

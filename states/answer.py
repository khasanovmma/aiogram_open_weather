from aiogram.dispatcher.filters.state import StatesGroup, State


class Answer(StatesGroup):
    user = State()

from aiogram.dispatcher.filters.state import StatesGroup, State


class CabinetForm(StatesGroup):
    corpus = State()
    number = State()

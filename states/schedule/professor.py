from aiogram.dispatcher.filters.state import StatesGroup, State


class ProfessorForm(StatesGroup):
    first_name = State()
    last_name = State()
    patronymic = State()
    email = State()
    telephone = State()



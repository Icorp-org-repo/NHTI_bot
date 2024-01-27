from aiogram.dispatcher.filters.state import StatesGroup, State


class LessonForm(StatesGroup):
    short_name = State()
    type_lesson = State()
    full_name = State()


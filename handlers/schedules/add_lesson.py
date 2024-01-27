from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from filters import IsActiveUser
from aiogram.dispatcher import FSMContext
from utils.db_api.commands import schedule_command
from keyboards.default.utils import get_buttons
from states.schedule import LessonForm


@dp.message_handler(IsActiveUser(), Command('add_lesson'))
async def add_lesson(message: types.Message):
    await message.answer('Привет, Добавим урок для Этого введите краткое название',
                         reply_markup=types.ReplyKeyboardRemove())
    await LessonForm.short_name.set()


@dp.message_handler(state=LessonForm.short_name)
async def state_short_name(message: types.Message, state: FSMContext):
    buttons_ =[['Лекция'],['Практика'], ['Лаба'], ['Экзамен']]
    answer = message.text
    short_name = answer
    await state.update_data(short_name=short_name)
    await message.answer(f"Тип урока: ", reply_markup=get_buttons(buttons_))
    await LessonForm.next() # Register.last_name.set()


@dp.message_handler(state=LessonForm.type_lesson)
async def state_type_lesson(message: types.Message, state: FSMContext):
    answer = message.text
    type_lesson = answer
    await state.update_data(type_lesson=type_lesson)
    button = 'None'
    await message.answer(f"Напиши польное название: ", reply_markup=get_buttons([[button]]))
    await LessonForm.next() # Register.last_name.set()


@dp.message_handler(state=LessonForm.full_name)
async def state_full_name(message: types.Message, state: FSMContext):
    answer = message.text
    full_name = None if answer == 'None' else answer
    await state.update_data(full_name=full_name)
    data = await state.get_data()
    await schedule_command.lesson_add(**data)
    await message.answer(f"Добавлен ", reply_markup=types.ReplyKeyboardRemove())
    await state.finish()

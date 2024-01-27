from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from filters import IsPrivateMessage, IsActiveUser
from aiogram.dispatcher import FSMContext
from utils.db_api.commands import schedule_command
from keyboards.default.utils import get_buttons
from states.schedule import ProfessorForm


@dp.message_handler(IsActiveUser(), IsPrivateMessage(), Command('add_professor'))
async def add_professor(message: types.Message):
    await message.answer('Привет, Добавим препода для Этого введите его имя',
                         reply_markup=types.ReplyKeyboardRemove())
    await ProfessorForm.first_name.set()


@dp.message_handler(state=ProfessorForm.first_name)
async def state_firs_name(message: types.Message, state: FSMContext):
    answer = message.text
    first_name = answer
    await state.update_data(first_name=first_name)
    await message.answer(f"Напиши фамилию препода: ", reply_markup=types.ReplyKeyboardRemove())
    await ProfessorForm.next() # Register.last_name.set()


@dp.message_handler(state=ProfessorForm.last_name)
async def state_last_name(message: types.Message, state: FSMContext):
    answer = message.text
    last_name = answer
    await state.update_data(last_name=last_name)
    await message.answer(f"Напиши отчество препода: ", reply_markup=types.ReplyKeyboardRemove())
    await ProfessorForm.next() # Register.last_name.set()


@dp.message_handler(state=ProfessorForm.patronymic)
async def state_patronymic(message: types.Message, state: FSMContext):
    answer = message.text
    patronymic = answer
    await state.update_data(patronymic=patronymic)
    button = 'None'
    await message.answer(f"Email если знаешь, иначе жми кнопку: ", reply_markup=get_buttons([[button]]))
    await ProfessorForm.next() # Register.last_name.set()


@dp.message_handler(state=ProfessorForm.email)
async def state_email(message: types.Message, state: FSMContext):
    answer = message.text
    email = None if answer == 'None' else answer
    await state.update_data(email=email)
    button = 'None'
    await message.answer(f"Email если знаешь, иначе жми кнопку: ", reply_markup=get_buttons([[button]]))
    await ProfessorForm.next() # Register.last_name.set()


@dp.message_handler(state=ProfessorForm.telephone)
async def state_telephone(message: types.Message, state: FSMContext):
    answer = message.text
    telephone = None if answer == 'None' else answer
    await state.update_data(telephone=telephone)
    data = await state.get_data()
    await schedule_command.professor_add(**data)
    await message.answer(f"Добавлен", reply_markup=types.ReplyKeyboardRemove())
    await state.finish() # Register.last_name.set()





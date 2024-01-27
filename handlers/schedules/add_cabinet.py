from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from filters import IsActiveUser
from aiogram.dispatcher import FSMContext
from utils.db_api.commands import schedule_command
from keyboards.default.utils import get_buttons
from states.schedule import CabinetForm

# class Cabinet(TimedBaseModel):
#     corpus = Column(String(2), nullable=False)
#     number = Column(Integer)


@dp.message_handler(IsActiveUser(), Command('add_cabinet'))
async def add_cabinet(message: types.Message):
    buttons_ = [['А', 'Б', 'В']]
    await message.answer('Укажите корпус',
                         reply_markup=get_buttons(buttons_))
    await CabinetForm.corpus.set()


@dp.message_handler(state=CabinetForm.corpus)
async def state_corpus(message: types.Message, state: FSMContext):
    answer = message.text
    corpus = answer
    await state.update_data(corpus=corpus)
    await message.answer(f"Введите Номер кабинета (число): ", reply_markup=types.ReplyKeyboardRemove())
    await CabinetForm.next()


@dp.message_handler(state=CabinetForm.number)
async def state_number(message: types.Message, state: FSMContext):
    answer = message.text
    if answer.isalnum():
        number = int(answer)
        await state.update_data(number=number)
        data = await state.get_data()
        await schedule_command.cabinet_add(**data)
        await state.finish()
        await message.answer(f"Добавлен ", reply_markup=types.ReplyKeyboardRemove())
    else:
        await message.answer(f"Введите число!!!: ", reply_markup=types.ReplyKeyboardRemove())
        await CabinetForm.number.set()

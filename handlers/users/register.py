from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram import types
from loader import dp
from states.default import Register
from keyboards.default.utils import get_buttons
from utils.db_api.commands import user_command
from filters.private_chat import IsPrivateMessage
from utils.misc import rate_limit


@rate_limit(limit=5)
@dp.message_handler(IsPrivateMessage(), Command('register'))
async def register(message: types.Message):
    try:
        button_ = message.from_user.first_name
    except Exception:
        button_ = 'None'
    try:
        user = await user_command.get_user(user_id=message.from_user.id)
        if user.first_name or user.last_name or user.email:
            await message.answer("Ты уже зарегистрирован для обновление данных воспользуйся /update_profile",
                                 reply_markup=get_buttons([['/update_profile']]))
        else:
            await message.answer('Привет, ты начал регистрацию, \n введи свое имя',
                                 reply_markup=get_buttons([[button_]]))
            await Register.first_name.set()
        if not user.is_active:
            await message.answer('Ты забанен', reply_markup=types.ReplyKeyboardRemove())
            await message.delete()
    except Exception:
        await user_command.add_user(user_id=message.from_user.id,
                                    name=message.from_user.username)
        await message.answer('Привет, ты начал регистрацию, \n введи свое имя', reply_markup=get_buttons([[button_]]))
        await Register.first_name.set()




@dp.message_handler(state=Register.first_name)
async def state_firs_name(message: types.Message, state: FSMContext):
    try:
        button_ = message.from_user.last_name
    except Exception:
        button_ = 'None'
    answer = message.text
    # Если пользователь ввель None то сохряняем None
    first_name = None if answer == 'None' else answer
    await state.update_data(first_name=first_name)
    await message.answer(f"{first_name}, напиши фамилию: ", reply_markup=get_buttons([[button_]]))
    await Register.next() # Register.last_name.set()


@dp.message_handler(state=Register.last_name)
async def state_last_name(message: types.Message, state: FSMContext):
    button_ = 'None'
    answer = message.text
    # Если пользователь ввель None то сохряняем None
    last_name = None if answer == 'None' else answer
    await state.update_data(last_name=last_name)
    data = await state.get_data()
    await message.answer(f"{data['first_name']} {last_name}. Введи свою почту: ", reply_markup=get_buttons([[button_]]))
    await Register.next()


@dp.message_handler(state=Register.email)
async def state_email(message: types.Message, state: FSMContext):
    answer = message.text
    email = None if answer == 'None' else answer
    await state.update_data(email=email)
    data = await state.get_data()
    await message.answer(f"Регистарция завершена")
    await user_command.update_user_all(message.from_user.id, first_name=data['first_name'],
                                       last_name=data['last_name'], email=data['email'])
    await state.finish()


from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from filters import IsPrivateMessage
from utils.misc.throttling import rate_limit
from utils.db_api.commands import user_command
from keyboards.default.utils import get_buttons


@rate_limit(limit=5)
@dp.message_handler(IsPrivateMessage(), Command('start'))
async def command_start(message: types.Message):
    try:
        user = await user_command.get_user(user_id=message.from_user.id)
        if user.is_active:
            await message.answer(f'Привет {message.from_user.full_name}!\n' 
                                 f'Твой id: {message.from_user.id}', reply_markup=types.ReplyKeyboardRemove())
        else:
            await message.answer('Ты забанен', reply_markup=types.ReplyKeyboardRemove())
            await message.delete()

    except Exception:
        await user_command.add_user(user_id=message.from_user.id,
                                    name=message.from_user.username)
        await message.answer('для работы пройдите регистрацию /register', reply_markup=get_buttons([['/register']]))

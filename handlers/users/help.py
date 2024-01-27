from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command


@dp.message_handler(Command('help'))
async def command_help(message: types.Message):
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Твой id: {message.from_user.id}')
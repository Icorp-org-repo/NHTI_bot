from aiogram import types
from loader import dp
from aiogram.dispatcher.filters import Command
from utils.db_api.commands import user_command


@dp.message_handler(Command('test'))
async def command_help(message: types.Message):
    await user_command.get_user(message.from_user.id)
    await user_command.get_commands(message.from_user.id)
    await message.answer(f'Привет {message.from_user.full_name}!\n'
                         f'Твой id: {message.from_user.id}')
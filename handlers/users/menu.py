from aiogram import types

from filters import IsPrivateMessage
from loader import dp
from aiogram.dispatcher.filters import Command
from utils.db_api.commands import user_command
from keyboards.default.utils import get_buttons


@dp.message_handler(IsPrivateMessage(), Command('menu'))
async def command_menu(message: types.Message):
    answer = await user_command.get_commands(message.from_user.id, True)
    command_names = list(answer.keys())
    text = '\n'.join([str(k) +' - '+ str(v) for k,v in answer.items()])
    await message.answer(f"Вы можете воспользоваться следующуи команды:\n{text}",
                         reply_markup=get_buttons(
                             [['/'+command_names[i + j] for i in range(2) if (i + j) < len(command_names)] for j in range(0, len(command_names), 2)]
                         ),
                         )

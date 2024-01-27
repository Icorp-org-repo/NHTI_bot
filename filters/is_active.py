from aiogram import types

from aiogram.dispatcher.filters import BoundFilter
from utils.db_api.commands import  user_command


class IsActiveUser(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        user = await user_command.get_user(message.from_user.id)
        return user.is_active

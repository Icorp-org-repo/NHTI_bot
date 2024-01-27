from aiogram import types

from aiogram.dispatcher.filters import BoundFilter


class IsPrivateCallback(BoundFilter):
    async def check(self, call: types.CallbackQuery) -> bool:
        return call.message.chat.type == types.ChatType.PRIVATE


class IsPrivateMessage(BoundFilter):
    async def check(self, message: types.Message) -> bool:
        return message.chat.type == types.ChatType.PRIVATE



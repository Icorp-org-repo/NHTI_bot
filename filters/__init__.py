from aiogram import Dispatcher

from .private_chat import IsPrivateMessage, IsPrivateCallback
from .is_active import IsActiveUser


def setup(dp: Dispatcher):
    dp.filters_factory.bind(IsPrivateMessage)
    dp.filters_factory.bind(IsPrivateCallback)
    dp.filters_factory.bind(IsActiveUser)

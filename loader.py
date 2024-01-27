from aiogram import Bot, Dispatcher, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from utils.db_api.db_gino import db
import config


# Переменная бота
storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN, parse_mode=types.ParseMode.HTML)
dp = Dispatcher(bot=bot, storage=storage)

__all__ = ['bot', 'storage', 'dp', 'db', 'config']

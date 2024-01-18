# ⣿⣿⣿⡿⠿⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠿⠿⢿⣿⣿⣿
# ⣿⣿⡟⠀⠀⠀⠀⠀⠉⠙⠿⣿⣿⣿⡿⢿⣿⣿⣿⠿⠋⠉⠀⢀⣀⠀⠀⢻⣿⣿
# ⣿⣿⠃⠀⢸⣿⣿⣶⡦⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠠⢶⣾⣿⣿⣇⠀⠘⣿⣿
# ⣿⣿⠀⠀⣼⡿⠟⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠻⢿⣿⠀⠀⣿⣿
# ⣿⣿⠀⠀⠋⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⠀⠀⣿⣿
# ⣿⣿⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣿⣿
# ⣿⠃⠀⠀⣀⣤⣶⣶⣶⣾⣷⣶⣦⡀⠀⠀⢀⣴⣿⣿⣿⣿⣿⣷⣦⣄⠀⠀⠘⣿
# ⠇⠀⣠⣾⣿⣿⣿⣿⡏⠉⢹⣿⣿⣷⠀⠀⣾⣿⣿⡏⠉⢹⣿⣿⣿⣿⣷⣄⠀⠘
# ⢀⣼⣿⣿⣿⣿⣿⣿⣷⣶⣾⣿⣿⠏⠀⠀⠹⣿⣿⣷⣶⣾⣿⣿⣿⣿⣿⣿⣷⡀
# ⣼⣿⣿⣿⣿⣿⣿⣿⠿⠛⠛⠉⠁⠀⠀⠀⠀⠈⠙⠛⠛⠿⣿⣿⣿⣿⣿⣿⣿⣧
# ⣻⣿⣿⣿⣿⣿⣿⠃⠀⠀⠀⠀⠀⢶⣶⣶⡶⠂⠀⠀⠀⠀⠘⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣦⣀⠀⠀⠀⠀⠀⣿⣿⠀⠀⠀⠀⠀⣀⣴⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⣀⠀⣿⣿⠀⣀⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿
# ⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿

from aiogram import Bot, Dispatcher, types, executor
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher import FSMContext
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton, ReplyKeyboardRemove, ContentType
from aiogram.utils.callback_data import CallbackData
import config

storage = MemoryStorage()
bot = Bot(token=config.BOT_TOKEN)
dp = Dispatcher(bot=bot, storage=storage)


@dp.message_handler()
async def hello_handler(message: types.Message) -> None:
    await bot.send_message(message.chat.id, 'Привет')

if __name__ == "__main__":
    executor.start_polling(
        dispatcher=dp,
        skip_updates=True,
    )
    input("Введи что угодно");
from aiogram import types

from loader import dp
from aiogram.dispatcher.filters import Command

from keyboards.inline.inline_kb_menu import ikb_menu, ikb_menu2
from keyboards.default.keyboard_menu import kb_menu
@dp.message_handler(Command('inline_menu'))
async def show_inline_menu(message:types.Message):
    await message.answer('Inline button down', reply_markup=ikb_menu)

@dp.callback_query_handler(text='Cообщение')
async def send_message(call: types.CallbackQuery):
    await call.message.answer('Kнопки заменены', reply_markup=kb_menu)


@dp.callback_query_handler(text='alert')
async def send_message(call: types.CallbackQuery):
    await call.answer('Kнопки заменены')


@dp.callback_query_handler(text='Кнопка2')
async def send_message(call: types.CallbackQuery):
    await call.message.edit_reply_markup(ikb_menu2)

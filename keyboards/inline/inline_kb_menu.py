from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


ikb_menu = InlineKeyboardMarkup(row_width=2,
                                inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Cooбщение', callback_data='Сообщение'),
                                        InlineKeyboardButton(text='Ссылка', url='https://www.youtube.com/watch?v=2Il_Ab-s0W8&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=5'),
                                    ],
                                    [
                                        InlineKeyboardButton(text='alert', callback_data='alert')
                                    ],
                                    [
                                        InlineKeyboardButton(text='Изменить', callback_data='Кнопка2')
                                    ]
                                ]
                                )

ikb_menu2 = InlineKeyboardMarkup(row_width=2,
                                 inline_keyboard=[
                                    [
                                        InlineKeyboardButton(text='Cooбщение', callback_data='Сообщение'),
                                        InlineKeyboardButton(text='Ссылка', url='https://www.youtube.com/watch?v=2Il_Ab-s0W8&list=PLPELDof3v08efHGT3gVLPCXG5cKRo50Nn&index=5'),
                                    ],
                                 ]
                                 )

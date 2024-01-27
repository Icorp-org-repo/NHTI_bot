from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


def get_buttons(list_name: list):
    """
    Принимает `Матрицу` из текста для создания кнопок
    Вывод происходить в следующем образом
    из [[button1, button2], [button3]]
    в
    button1 | button2
        button3
    :param list_text:
    :return: создает копки
    """
    kb = ReplyKeyboardMarkup(resize_keyboard=True)
    for names in list_name:
        flag = True
        for name in names:
            button_ = KeyboardButton(text=name)
            if flag:
                kb.add(button_)
                flag = False
            else:
                kb.insert(button_)
    return kb
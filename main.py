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

from aiogram import executor


async def on_start(dp):
    '''
    Запуск при старте
    :param dp: Диспетчер
    :return: None
    '''
    import filters
    filters.setup(dp)

    import middlewares
    middlewares.setup(dp)

    from loader import db
    from utils.db_api.db_gino import on_startup
    print('Подключение к PostgreSQL')
    await on_startup(dp)
    # print('Удаление всех данных')
    # await db.gino.drop_all()
    print('Создания таблиц')
    await db.gino.create_all()


    # Отправка сообщение о запуске
    from utils.notify_admins import on_startup_notify
    await on_startup_notify(dp)

    # Установка комманд
    # from utils.set_bot_commands import set_default_commands
    # await set_default_commands(dp)

    print('Бот запущен')


if __name__ == "__main__":
    from handlers import dp
    executor.start_polling(
        dispatcher=dp,
        on_startup=on_start
    )
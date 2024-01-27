from asyncpg import UniqueViolationError
from datetime import datetime
from utils.db_api.db_gino import db
from ..schemas import User, Role, UserRoles, Command, RoleCommands


async def add_user(user_id: int, name: str,
                   first_name: str | None = None,
                   last_name: str | None = None,
                   email: str | None = None) -> None:
    """
    Добавить Пользователя
    :param user_id: id пользователя
    :param name: Nike name
    :param first_name: имя ползователя
    :param last_name: фамилия пользователя
    :param email: почта пользователя
    :return: None
    """
    try:
        user = User(id=user_id, name=name, first_name=first_name, last_name=last_name, email=email,
                    is_active=True, is_admin=False)
        await user.create()
    except UniqueViolationError:
        print('Пользователь не добавлен')


async def select_all_users():
    users = await User.query.gino.all()
    return users


async def count_user():
    count = db.func.count(User.user_id).gino.scalar()
    return count


async def get_user(user_id):
    user = await User.query.where(User.id == user_id).gino.first()
    print(user)
    return user


async def update_user_all(user_id,
                          first_name: str | None = None,
                          last_name: str | None = None,
                          email: str | None = None):
    user = await get_user(user_id)
    await user.update(first_name=first_name, last_name=last_name,email=email).apply()


async def get_commands(user_id:int, is_private:bool = False):
    """
    Возвращает доступные команды пользователя
    :param user_id:
    :param is_private: Если True то вернет все комманды, Иначе вернет только комманды для чата
    :return: Комманды
    """
    commands = dict()
    sql = UserRoles.query.where(UserRoles.user_id == user_id)
    roles_user = await sql.gino.all()
    for item in roles_user:
        roleID = item.role_id
        sql_ = RoleCommands.query.where(RoleCommands.role_id == roleID)
        roles_commands = await sql_.gino.all()
        for item_ in roles_commands:
            commandsID = item_.command_id
            command = await Command.query.where(Command.id == commandsID).gino.first()
            if is_private:
                commands[command.name] = command.description
            elif not command.is_private:
                commands[command.name] = command.description
    return commands


async def get_command(command_id:int ):
    pass

from sqlalchemy import Column, BigInteger, String, Text, ForeignKey, BOOLEAN

from utils.db_api.db_gino import TimedBaseModel


class User(TimedBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(128), )
    first_name = Column(String(128),)
    last_name = Column(String(128), )
    email = Column(String(256),)
    is_active = Column(BOOLEAN,)
    is_admin = Column(BOOLEAN,)


class Role(TimedBaseModel):
    __tablename__ = 'roles'
    id = Column(BigInteger, primary_key=True)
    title = Column(String(256),)
    description = Column(Text,)


class Command(TimedBaseModel):
    __tablename__ = 'commands'
    id = Column(BigInteger, primary_key=True)
    name = Column(String(32),)
    is_private= Column(BOOLEAN,)
    description = Column(Text, )


class UserRoles(TimedBaseModel):
    __tablename__ = 'users_roles'
    id = Column(BigInteger, primary_key=True)
    user_id = Column(BigInteger, ForeignKey("users.id"),)
    role_id = Column(BigInteger, ForeignKey("roles.id"), )


class RoleCommands(TimedBaseModel):
    __tablename__ = 'roles_commands'
    id = Column(BigInteger, primary_key=True)
    role_id = Column(BigInteger, ForeignKey("roles.id"))
    command_id = Column(BigInteger, ForeignKey("commands.id"))

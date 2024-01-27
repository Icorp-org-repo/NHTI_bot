from asyncpg import UniqueViolationError
from datetime import datetime
from utils.db_api.db_gino import db
from ..schemas import Schedule, Professor, Examine, Lesson, Cabinet


async def schedule_find_day(day_week: int, period: int):
    sql = Schedule.query.where(Schedule.day_week == day_week, Schedule.period_week == period)
    print(sql)
    schedules = await sql.gino.all()
    return schedules


async def professor_find(first_name: str,
                         last_name: str,
                         patronymic: str,):
    sql = Professor.query
    if last_name:
        sql = sql.where(Professor.last_name == last_name)
    if first_name:
        sql = sql.where(Professor.first_name == first_name)
    if patronymic:
        sql = sql.where(Professor.patronymic == patronymic)
    print(sql)
    professors = await sql.gino.all()
    return professors


async def select_all_professor():
    professors = await Professor.query.gino.all()
    return professors


async def professor_add(first_name: str,
                        last_name: str,
                        patronymic: str,
                        email: str | None = None,
                        telephone: str | None = None) -> None:
    """
    Добавить профессора
    :param first_name: Имя
    :param last_name: Фамилия
    :param patronymic: Отчество
    :param email: Почта
    :param telephone: Телефонный номер
    :return: None
    """
    try:
        professor = Professor(first_name=first_name,
                              last_name=last_name, patronymic=patronymic,
                              email=email, telephone=telephone)
        await professor.create()
    except UniqueViolationError:
        print('Профессор не добавлен')


async def lesson_find(short_name: str,
                      type_les: str,):
    sql = Lesson.query
    if type_les:
        sql = sql.where(Lesson.type_lesson == type_les)
    if short_name:
        sql = sql.where(Lesson.first_name == short_name)
    print(sql)
    lessons = await sql.gino.all()
    return lessons


async def select_all_lesson():
    lessons = await Lesson.query.gino.all()
    return lessons


async def lesson_add(short_name: str,
                     type_lesson: str,
                     full_name: str | None = None) -> None:
    """
    Добавить урок
    :param short_name: Карткое название
    :param type_lesson: Тип занятия (Лекция, Практика, Лаба, Экзамен)
    :param full_name:
    :return: None
    """
    try:
        lesson = Lesson(short_name=short_name,
                        type_lesson=type_lesson, full_name=full_name)
        await lesson.create()
    except UniqueViolationError:
        print('Урок не добавлен')


async def schedule_add(day_week: str,
                       period_week: str,
                       lesson_id: int,
                       professor_id: int,
                       cabinet_id: int,
                       start_time: datetime.time,
                       end_time = None) -> None:
    """
    Добавить расписание
    :param day_week: День недели
    :param period_week: Период недели
    :param lesson_id: id урока
    :param professor_id: id профессора
    :param cabinet_id: id кабинета
    :param start_time: время начало
    :param end_time: время конца
    :return: None
    """
    try:
        schedule = Schedule(day_week=day_week,
                            period_week=period_week,
                            lesson_id=lesson_id,
                            professor_id=professor_id,
                            cabinet_id=cabinet_id,
                            start_time=start_time,
                            end_time=end_time)
        await schedule.create()
    except UniqueViolationError:
        print('Расписание не добавлен')


async def examine_add(lesson_id: int,
                      professor_id: int,
                      cabinet_id: int,
                      date_start: datetime.date,
                      start_time: datetime.time,
                      end_time = None) -> None:
    """
    Добавить расписание
    :param lesson_id: id урока
    :param professor_id: id профессора
    :param cabinet_id: id кабинета
    :param date_start: дате
    :param start_time: время начало
    :param end_time: время конца
    :return: None
    """
    try:
        schedule = Examine(lesson_id=lesson_id,
                           professor_id=professor_id,
                           cabinet_id=cabinet_id,
                           date_start=date_start,
                           start_time=start_time,
                           end_time=end_time)
        await schedule.create()
    except UniqueViolationError:
        print('Расписание не добавлен')


async def cabinet_add(corpus:str, number:int) -> None:
    """
    Добавить кобинет
    :param corpus: Корпус
    :param number: Номер кабинета
    :return: None
    """
    try:
        cabinet = Cabinet(corpus=corpus, number=number)
        await cabinet.create()
    except UniqueViolationError:
        print('Кабинет не добавлен')

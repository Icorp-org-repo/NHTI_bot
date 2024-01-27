from sqlalchemy import Column,Date, Time, Integer, BigInteger, String, Text, ForeignKey

from utils.db_api.db_gino import TimedBaseModel


class Professor(TimedBaseModel):
    __tablename__ = "professors"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    first_name = Column(String(128), )
    last_name = Column(String(128), nullable=False)
    patronymic = Column(String(128), )
    email = Column(String(256), )
    telephone = Column(String(15),)


class Lesson(TimedBaseModel):
    __tablename__ = "lessons"
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    full_name = Column(String(256), )
    short_name = Column(String(16), nullable=False)
    type_lesson = Column(String(16), nullable=False)


class Cabinet(TimedBaseModel):
    __tablename__ = 'cabinets'
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    corpus = Column(String(2), nullable=False)
    number = Column(Integer)


class Schedule(TimedBaseModel):
    __tablename__ = 'schedules'
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    day_week = Column(Integer, nullable=False)
    period_week = Column(Integer, )
    lesson_id = Column(BigInteger, ForeignKey('lessons.id'), nullable=False)
    cabinet_id = Column(BigInteger, ForeignKey('cabinets.id'), nullable=False)
    professor_id = Column(BigInteger, ForeignKey('professors.id'), nullable=False)
    start_time = Column(Time)
    end_time = Column(Time)


class Examine(TimedBaseModel):
    __tablename__ = 'examines'
    id = Column(BigInteger, primary_key=True, index=True, autoincrement=True)
    lesson_id = Column(BigInteger, ForeignKey('lessons.id'), nullable=False)
    cabinet_id = Column(BigInteger, ForeignKey('cabinets.id'), nullable=False)
    professor_id = Column(BigInteger, ForeignKey('professors.id'), nullable=False)
    date_start = Column(Date)
    start_time = Column(Time)
    end_time = Column(Time)

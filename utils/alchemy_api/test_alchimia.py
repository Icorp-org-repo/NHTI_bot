from sqlalchemy import create_engine, select, Table, Column, Integer, String, MetaData, ForeignKey, DECIMAL

import config

meta = MetaData()

authors = Table('Authors', meta,
                Column('id', Integer, primary_key=True),
                Column('name', String(250), nullable=False)
                )

Books = Table('Books', meta,
              Column('id', Integer, primary_key=True,),
              Column('title', String(250), nullable=False),
              Column('author_id', Integer, ForeignKey('Authors.id')),
              Column('genre', String(250)),
              Column('price', DECIMAL(12, 2))
              )


engine = create_engine(config.POSTGRES_URI, echo=True)
# В meta записываем данные
meta.create_all(engine)

conn = engine.connect()


if __name__ == '__main__':
    pass

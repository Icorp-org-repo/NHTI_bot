import sqlite3


class DBConnector:
    def __new__(cls, *args, **kwargs):
        if not hasattr(cls, 'instance'):
            cls.instance = super(DBConnector, cls).__new__(cls, *args, **kwargs)
        return cls.instance

    def __init__(self):
        self._conn = sqlite3.connect('myDataBase.db') # Подключение к БД

    def fetch(self, query):
        cursor = self._conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

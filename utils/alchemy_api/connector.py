from sqlalchemy import create_engine, engine, future


class DBConnector:

    def __init__(self, engin: engine.mock.MockConnection | future.engine.Engine | engine.Engine):

        self._conn = None # Подключение к БД

    def fetch(self, query):
        cursor = self._conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()
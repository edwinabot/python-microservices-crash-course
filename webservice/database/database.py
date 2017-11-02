# pylint: disable=E1101
"""
This module has the functions to create a dabatabase
"""
import sqlite3

from settings import db_name, db_path

def create_database():
    """
    Creates a sqlite DB and its tables
    """
    conn = sqlite3.connect(f'{db_path}/{db_name}')
    query = "CREATE TABLE photos("\
            "id INTEGER PRIMARY KEY AUTOINCREMENT,"\
            "albumId INTEGER,"\
            "title VARCHAR(255),"\
            "thumbnailUrl VARCHAR(2000),"\
            "url VARCHAR(2000));"
    cursor = conn.execute(query)
    cursor.close()
    conn.close()

class Database:
    _db_path = db_path + db_name
    _connection = None
    _cursor = None

    def _open(self):
        if self._connection:
            self.close()
        self._connection = sqlite3.connect(db_path + db_name)
        self._cursor = self._connection.cursor()
        return self._cursor

    def _close(self):
        if self._connection:
            self._cursor.close()
            self._cursor = None
            self._connection.commit()
            self._connection.close()
            self._connection = None

    def execute(self, action):
        return self._cursor.execute(action.create_statement())

    def execute_many(self, actions):
        return [self.execute(action) for action in actions]

    def __enter__(self):
        self._open()
        return self

    def __exit__(self, exception_type, exception_value, traceback):
        self._close()

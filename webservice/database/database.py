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

    @classmethod
    def _open(cls):
        if cls._connection:
            cls.close()
        cls._connection = sqlite3.connect(db_path + db_name)
        return cls._connection.cursor()

    @classmethod
    def _close(cls):
        if cls._connection:
            cls._connection.close()
            cls._connection = None

    @classmethod
    def execute(cls, action):
        try:
            cursor = cls._open()
            cursor.execute(action.create_statement())
            result = cursor.lastrowid
        except Exception as ex:
            raise ex
        finally:
            cls._close()
        return result

    @classmethod
    def execute_many(cls, actions):
        raise NotImplementedError()

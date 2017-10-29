# pylint: disable=E1101
"""
This module has the functions to create a dabatabase
"""
import sqlite3

def create_database(db_path, db_name):
    """
    Creates a sqlite DB and its tables
    """
    conn = sqlite3.connect(f'{db_path}/{db_name}')
    query = "CREATE TABLE photos("\
            "id INTEGER PRIMARY KEY,"\
            "albumId INTEGER,"\
            "title VARCHAR(255),"\
            "thumbnailUrl VARCHAR(2000),"\
            "url VARCHAR(2000));"
    cursor = conn.execute(query)
    cursor.close()
    conn.close()

class Database:

    def __init__(self, db_name, db_path):
        self._db = db_path + db_name
        self._conn = None

    def open(self):
        self._conn = sqlite3.connect(self._db)

    def close(self):
        self._conn.close()

    def execute_action(self, action):
        raise NotImplementedError()

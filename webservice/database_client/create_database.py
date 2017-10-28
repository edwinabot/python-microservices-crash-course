# pylint: disable=C0103
"""
This script creates the database and its tables.
"""
import sqlite3

def create_database(db_path, db_name):
    """
    Creates a sqlite DB and its tables
    """
    #conn = sqlite3.connect(f'{db_path}/{db_name}')
    conn = sqlite3.connect()
    conn.execute_script('create_tables.sql')

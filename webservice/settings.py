"""
This module has all the settings variables for our webservice
"""

db_path = './webservice/'
db_name = 'photos.sqlite3'

try:
    from local_settings import *
except ImportError:
    pass

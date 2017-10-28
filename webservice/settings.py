# pylint: disable=C0103, W0401
"""
This module has all the settings variables
for our webservice
"""

db_path = './'
db_name = 'photos.sqlite3'

try:
    from local_settings import *
except ImportError:
    pass

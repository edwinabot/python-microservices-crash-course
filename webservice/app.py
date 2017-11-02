"""
This module contains the entry point of our service
"""
import os.path
from wsgiref.simple_server import make_server

import falcon

from resources.photo_resource import PhotoResource
from database.database import create_database
import settings

api = falcon.API()
api.add_route('/photo/{photo_id}', PhotoResource())
api.add_route('/photo', PhotoResource())

if __name__ == '__main__':
    print('Serving app at http://localhost:8200')

    if not os.path.isfile(settings.db_path + settings.db_name):
        create_database()

    server = make_server('localhost', 8200, api)
    server.serve_forever()

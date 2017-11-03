"""
This module contains the entry point of our service
"""
import os.path
from wsgiref.simple_server import make_server
from multiprocessing.dummy import Process

import falcon

from resources.photo_resource import PhotoResource
from database.database import create_database
from photos_sandbox_client import PhotosSandboxClient
import settings

api = falcon.API()
api.add_route('/photo/{photo_id}', PhotoResource())
api.add_route('/photo', PhotoResource())

if __name__ == '__main__':

    if not os.path.isfile(settings.db_path + settings.db_name):
        create_database()

    photos_client = PhotosSandboxClient('https://jsonplaceholder.typicode.com/photos')

    photos_fetching_process = Process(target=photos_client)

    server = make_server('localhost', 8200, api)
    print('Serving app at http://localhost:8200')

    photos_fetching_process.run()
    server.serve_forever()

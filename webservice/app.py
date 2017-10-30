"""
This module contains the entry point of our service
"""
from wsgiref.simple_server import make_server

import falcon

from resources.photo_resource import PhotoResource

api = falcon.API()
api.add_route('/photo', PhotoResource())

if __name__ == '__main__':
    print('Lets build some webservices')
    server = make_server('localhost', 8200, api)
    server.serve_forever()

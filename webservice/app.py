"""
This module contains the entry point of our service
"""
from wsgiref.simple_server import make_server

import falcon


class PhotoResource:
    """
    REST resource for Photos
    """
    def on_get(self, request, response):
        """Handles GET requests"""
        photo = {
            "albumId": 1,
            "id": 2,
            "title": "reprehenderit est deserunt velit ipsam",
            "url": "http://placehold.it/600/771796",
            "thumbnailUrl": "http://placehold.it/150/771796"
        }

        response.media = photo


api = falcon.API()
api.add_route('/photo', PhotoResource())

if __name__ == '__main__':
    print('Lets build some webservices')
    server = make_server('localhost', 8200, api)
    server.serve_forever()

import json

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

    def on_post(self, request: falcon.Request, response: falcon.Response):
        """Handles POST requests"""
        doc = json.load(request.bounded_stream)
        response.status = falcon.HTTP_OK
        response.body = json.dumps(doc)

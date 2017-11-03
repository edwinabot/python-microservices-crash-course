import json

import falcon

from database.database import Database
from database.photo_model import PhotoModel

from database.actions.insert_photo_action import InsertPhotoAction
from database.actions.get_photo_by_id_action import GetPhotoByIdAction


class PhotoResource:
    """
    REST resource for Photos
    """

    def on_get(self, request: falcon.Request, response: falcon.Response, photo_id: int):
        """Handles GET requests"""

        with Database() as db:
            action = GetPhotoByIdAction(photo_id)
            result = db.execute(action).fetchone()

        photo = PhotoModel(*result)
        response.status = falcon.HTTP_OK
        response.body = json.dumps(photo.as_dict())

    def on_post(self, request: falcon.Request, response: falcon.Response):
        """Handles POST requests"""
        doc = json.load(request.bounded_stream)
        photo = PhotoModel(photo_id=doc['id'],
                           album_id=doc['albumId'],
                           title=doc['title'],
                           url=doc['url'],
                           thumbnail_url=doc['thumbnailUrl'])

        with Database() as db:
            action = InsertPhotoAction(photo)
            result = db.execute(action).lastrowid

        response.status = falcon.HTTP_OK
        response.body = json.dumps({'url': f'{request.uri}/{result}'})

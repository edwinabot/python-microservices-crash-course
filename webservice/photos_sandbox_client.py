from collections.abc import Callable

import requests
from database.photo_model import PhotoModel
from database.database import Database
from database.actions.insert_photo_action import InsertPhotoAction

class PhotosSandboxClient(Callable):

    def __init__(self, url):
        self._url = url

    def fetch_photos(self):
        photos_json = requests.get(self._url).json()
        photo_models = [PhotoModel(*photo.values()) for photo in photos_json]
        with Database() as db:
            actions = [InsertPhotoAction(photo_model) for photo_model in photo_models]
            db.execute_many(actions)

    def __call__(self, *args, **kwargs):
        self.fetch_photos()

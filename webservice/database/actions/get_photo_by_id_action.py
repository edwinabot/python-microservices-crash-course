from database.actions.abstract_action import DatabaseAction
from database.photo_model import PhotoModel

class GetPhotoByIdAction(DatabaseAction):

    def __init__(self, photo_id: int):
        self._photo_id = photo_id

    def create_statement(self):

        query = f"SELECT * FROM photos WHERE id = {self._photo_id};"

        return query

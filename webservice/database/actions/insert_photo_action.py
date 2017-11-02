from database.actions.abstract_action import DatabaseAction
from database.photo_model import PhotoModel


class InsertPhotoAction(DatabaseAction):

    def __init__(self, photo: PhotoModel):
        self._photo = photo

    def create_statement(self):

        query = "INSERT INTO photos("\
                "albumId, "\
                "title, "\
                "thumbnailUrl, "\
                "url) "\
                "VALUES "\
                f'({self._photo.album_id}, '\
                f'"{self._photo.title}", '\
                f'"{self._photo.thumbnail_url}", '\
                f'"{self._photo.url}");'

        return query

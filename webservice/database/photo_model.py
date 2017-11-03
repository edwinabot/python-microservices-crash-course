class PhotoModel:
    def __init__(self, album_id, photo_id, title, url, thumbnail_url):
        self._photo_id = photo_id
        self._album_id = album_id
        self._title = title
        self._url = url
        self._thumbnail_url = thumbnail_url

    @property
    def photo_id(self):
        return self._photo_id

    @property
    def album_id(self):
        return self._album_id

    @property
    def title(self):
        return self._title

    @property
    def url(self):
        return self._url

    @property
    def thumbnail_url(self):
        return self._thumbnail_url

    def as_dict(self):
        return {'photo_id': self.photo_id,
                'album_id': self.album_id,
                'title': self.title,
                'url': self.url,
                'thumbnail_url': self.thumbnail_url}

from platform import python_version

from instapy_cli.api import InstapySession
from instapy_cli.media import Media

'''
TODO:
- use commented part of code to upload a photo from local image or link
- download media and use the path, then remove the media
- create a new module to handle media files and links
'''
class InstapyCli(object):
    def __init__(self, username, password):
        self._session = InstapySession()
        self._session.login(username, password)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def upload(self, file, caption=''):
        media = Media(file)
        path = media.getPath()

        try:
            media_id = self._session.upload_photo(path)
            self._session.configure_photo(media_id, caption)
        finally:
            pass

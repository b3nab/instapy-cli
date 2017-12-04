from platform import python_version

from instapy_cli.api import InstapySession


class InstapyCli(object):
    def __init__(self, username, password):
        self._session = InstapySession()
        self._session.login(username, password)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def upload(self, path, caption=''):
        media_id = self._session.upload_photo(path)
        self._session.configure_photo(media_id, caption)
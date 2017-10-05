from instapy_cli.session import PynstagramSession


class PynstagramClient(object):
    def __init__(self, username, password):
        self._session = PynstagramSession()
        self._session.login(username, password)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def upload(self, path, caption=''):
        media_id = self._session.upload_photo(path)
        self._session.configure_photo(media_id, caption)
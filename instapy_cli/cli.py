from platform import python_version

from instapy_cli.api import InstapySession
from instapy_cli.media import Media

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
        upload_completed = True

        try:
            media_id = self._session.upload_photo(path)
            self._session.configure_photo(media_id, caption)
        except Exception as e:
            print('Error is >>\n    ' + str(e))
            print('\nSomething went bad.\nPlease retry or send an issue on https://github.com/b3nab/instapy-cli\n')
            upload_completed = False
        finally:
            if upload_completed:
                print('Done.')
            # media_status = 'YES' if media.isDownloaded() else 'NO'
            # print('Media is a downloaded file? ' + media_status)
            if media.isDownloaded():
                media.removeMedia()
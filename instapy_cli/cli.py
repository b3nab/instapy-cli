import os, json, codecs, datetime
from platform import python_version
from instagram_private_api import (
        Client, ClientError, ClientLoginError,
        ClientCookieExpiredError, ClientLoginRequiredError )
from instapy_cli.media import Media
import warnings
warnings.filterwarnings("ignore")

class InstapyCli(object):
    settings = 'ig.json'
    def __init__(self, username, password, cookie=None):
        self._login(username, password, cookie)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass
    
    def _login(self, username, password, cookie):
        device_id = None
        try:
            if cookie:
                print('[IG] Use cookie.')
                self.client = Client(
                    username, password,
                    settings=cookie)
            if not os.path.isfile(self.settings):
                # settings file does not exist
                print('[IG] Unable to find file: {0!s}'.format(self.settings))

                # login new
                self.client = Client(
                    username, password,
                    on_login=lambda x: self._write_ig_settings(x, self.settings))
            else:
                # with open(settings_file) as file_data:
                #     cached_settings = json.load(file_data, object_hook=from_json)
                cached_settings = self._get_ig_settings()
                print('Reusing settings: {0!s}'.format(self.settings))

                device_id = cached_settings.get('device_id')
                # reuse auth settings
                self.client = Client(
                    username, password,
                    settings=cached_settings)
            # with cookie
            # self.client = Client(user, password, cookie=self._get_ig_settings())
        # except ClientCookieExpiredError as e:
        #     self.client = Client(user, password)
        #     self._write_ig_cookie(self.client.settings['cookie'])
        except (ClientCookieExpiredError, ClientLoginRequiredError) as e:
            print(
                'ClientCookieExpiredError/ClientLoginRequiredError: {0!s}'.format(e))

            # Login expired
            # Do relogin but use default ua, keys and such
            self.client = Client(
                username, password,
                device_id=device_id,
                on_login=lambda x: self._write_ig_settings(x, self.settings))

        except ClientLoginError as e:
            print('ClientLoginError {0!s}'.format(e))
            exit(9)
        except ClientError as e:
            print('ClientError {0!s} (Code: {1:d}, Response: {2!s})'.format(
                e.msg, e.code, e.error_response))
            exit(9)
        except Exception as e:
            print('Unexpected Exception: {0!s}'.format(e))
            exit(99)
        # finally:
        #     print(self.client.current_user())
    
    def set_cookie(self, cookie):
        self.settings = cookie
    
    def _get_ig_settings(self):
        with open(self.settings, 'r') as igSettings:
            cached_settings = json.load(igSettings, object_hook=self.from_json)
            return cached_settings

    def _write_ig_settings(self, api, settings):
        # self.cookie = cookie
        with open(self.settings, 'w') as igSettings:
            json.dump(api.settings, igSettings, default=self.to_json)
            print('SAVED: {0!s}'.format(settings))
            # igSettings.write(cookie)
    
    def to_json(self, python_object):
        if isinstance(python_object, bytes):
            return {'__class__': 'bytes',
                    '__value__': codecs.encode(python_object, 'base64').decode()}
        raise TypeError(repr(python_object) + ' is not JSON serializable')

    def from_json(self, json_object):
        if '__class__' in json_object and json_object['__class__'] == 'bytes':
            return codecs.decode(json_object['__value__'].encode(), 'base64')
        return json_object
    
    def upload(self, file, caption='', story=False):
        upload_completed = True
        media = Media(file)

        res = None
        try:
            
            if media.is_image():
                image_data, image_size = media.prepare(story)
                # print('image size: {} with ratio of: {}'.format(image_size, image_size[0]/image_size[1]))
                if story:
                    res = self.client.post_photo_story(image_data, image_size)
                else:
                    res = self.client.post_photo(image_data, image_size, caption=caption)
            elif media.is_video():
                video_data, video_size, video_duration, video_thumbnail = media.prepare(story)
                if story:
                    res = self.client.post_video_story(video_data, video_size, video_duration, video_thumbnail)
                else:
                    res = self.client.post_video(video_data, video_size, video_duration, video_thumbnail, caption=caption)
            else:
                raise Exception('Media is not a recognized file type, use only images and videos.')
                
            # print(res)
            

        except Exception as e:
            print('Error is >>\n    ' + str(e))
            print('\nSomething went bad.\nPlease retry or send an issue on https://github.com/b3nab/instapy-cli\n')
            upload_completed = False

        finally:
            # media_status = 'YES' if media.isDownloaded() else 'NO'
            # print('Media is a downloaded file? ' + media_status)
            if media.isDownloaded():
                media.removeMedia()
            if upload_completed:
                print('Done.')
            else:
                raise IOError("Unable to upload.")
            return res

import os, requests
from instagram_private_api import MediaRatios
from instagram_private_api_extensions import media as IGMedia
import filetype
#import urlparse for Python2 and Python3
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse

MIN_ASPECT_RATIO = 0.80
MAX_ASPECT_RATIO = 1.91

class Media(object):
    media_path = None
    media = None
    media_ext = None
    isLink = False

    def __init__(self, file, ratio='post'):
        # if file is link
        if urlparse(file).scheme in ('http', 'https'):
            self.media_path = self.downloadMediaFromLink(file)
            self.isLink = True
        # if file is a local file
        else:
            self.media_path = file
        
        self.check_type()
    
    def check_type(self):
        self.media_ext = filetype.guess(self.media_path).extension
    
    def is_image(self):
        return True if self.media_ext in ['jpg', 'png', 'gif'] else False
        
    def is_video(self):
        return True if self.media_ext in ['mp4', 'mov', 'avi'] else False

    def prepare(self, story=False):
        ratio = MediaRatios.reel if story else MediaRatios.standard
        size = (1080, 1920) if story else (1080, 1350)
        # print('ratio is: ', ratio)
        if self.is_image():
            return IGMedia.prepare_image(self.media_path, max_size=size, aspect_ratios=ratio)
        elif self.is_video():
            max_time = 15.0 if story else 60.0
            return IGMedia.prepare_video(self.media_path, max_size=size, aspect_ratios=ratio, max_duration=max_time)

    def isDownloaded(self):
        return self.isLink

    def downloadMediaFromLink(self,url):
        print('Downloading Media..')
        # print(urlparse(url))
        fileName = urlparse(url).path.split('/')[-1]
        # print(fileName)
        r = requests.get(url, allow_redirects=True)
        open(fileName, 'wb').write(r.content)
        return fileName

    def removeMedia(self):
        os.remove(self.media_path)

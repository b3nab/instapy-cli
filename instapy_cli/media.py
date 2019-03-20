import os, requests
from PIL import Image
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
    media_type = None
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
        self.apply_fix()
    
    def check_type(self):
        if self.media_path.split('.')[-1] in ['jpg', 'jpeg', 'png']:
            self.media_type = 'img'
        elif self.media_path.split('.')[-1] in ['mp4', 'mov']:
            self.media_type = 'vid'
        
    def apply_fix(self):
        if self.media_type == 'vid':
            pass
        elif self.media_type == 'img':
            self.media = Image.open(self.media_path)
            if self.need_ratio_fix(self.media):
                self.media = self.fix_aspect_ratio(self.media)
            # new_object.save("optimized.jpg", "JPEG", quality=100, optimize=True, progressive=True)
    
    def get_ratio(self, width, height):
        return width/height
    
    def data(self):
        return self.media

    def size(self):
        return (self.width, self.height)
    
    def duration(self):
        return 0
    
    def thumbnail(self):
        return 0
    
    def need_ratio_fix(self, img):
        ratio = self.get_ratio(img.size[0], img.size[1])
        if ratio < MIN_ASPECT_RATIO or ratio > MAX_ASPECT_RATIO:
            return True
        return False

    def fix_aspect_ratio(self, original_img):
        width, height = original_img.size
        aspect_ratio = self.get_ratio(width, height)

        if aspect_ratio < MIN_ASPECT_RATIO:
            # Add equal black borders on the right and left 
            new_width = MIN_ASPECT_RATIO * height
            left = 0 - ((new_width - width) / 2)
            top = 0
            right = width + ((new_width - width) / 2)
            bottom = height
            newImage = self.cropImage(left, top, right, bottom, original_img)
            return newImage
        elif aspect_ratio > MAX_ASPECT_RATIO:
            # Add equal black borders on top and bottom 
            new_height = width / MAX_ASPECT_RATIO
            left = 0
            top = 0 - ((new_height - height) / 2)
            right = width
            bottom = height + ((new_height - height) / 2)
            newImage = self.cropImage(left, top, right, bottom, original_img)
            return newImage
        else:
            return original_img

    def cropImage(self, left, top, right, bottom, imageObject):
        area = (left, top, right, bottom)
        return imageObject.convert('RGB').crop(area)
    
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

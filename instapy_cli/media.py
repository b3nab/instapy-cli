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
    pathFile = None
    optimizedImage = None
    media = None
    isLink = False

    def __init__(self, file):
        self.media = file
        # if file is link
        if urlparse(file).scheme in ('http', 'https'):
            self.pathFile = self.downloadMediaFromLink(file)
            self.isLink = True

        # if file is a local file
        else:
            self.pathFile = file

        original_image_object = Image.open(self.pathFile)
        print("Fixing aspect ratio if not according to accepted dimensions..")
        new_object = self.fixAspectRatio(original_image_object)
        print("Generating and saving optimized image..")
        new_object.save("optimized.jpg", "JPEG", quality=100, optimize=True, progressive=True)
        self.optimizedImage = "optimized.jpg"

    def getPath(self):
        return self.optimizedImage

    def fixAspectRatio(self, original_img):
        width, height = original_img.size
        aspect_ratio = width/height

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
        return imageObject.crop(area)
    
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
        os.remove(self.pathFile)
        os.remove(self.optimizedImage)

import os, requests
#import urlparse for Python2 and Python3
try:
    from urllib.parse import urlparse
except ImportError:
    from urlparse import urlparse


class Media(object):
    pathFile = None
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

    def getPath(self):
        return self.pathFile

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

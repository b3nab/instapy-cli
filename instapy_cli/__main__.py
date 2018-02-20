import sys
from platform import python_version
from instapy_cli.cli import InstapyCli as client
from optparse import OptionParser
import pkg_resources  # part of setuptools
version = pkg_resources.require('instapy_cli')[0].version


'''
TODO:
- use instapy_cli.media to download image link and use it for upload and configure_photo
- rewrite main to support file and links for media
'''
def main(args=None):

    welcome_msg = 'instapy-cli'
    print('instapy-cli v.' + version)
    print('Python version: ' + python_version())

    # cli = client()
    # cli.loop(args)

    if args is None:
        print('use >> instapy -u <USERNAME> -p <PASSWORD> -f <IMAGE.JPG> -t <CAPTION>')
        args = sys.argv[1:]
    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option('-u', dest='username', help='username')
    parser.add_option('-p', dest='password', help='password')
    parser.add_option('-f', dest='file', help='file path or url')
    # parser.add_option('-u', dest='url', help='url to media')
    parser.add_option('-t', dest='caption', help='caption text')

    (options, args) = parser.parse_args(args)
    if not options.username:
        parser.error('Username is required')
    password = options.password
    if not options.password:
      import getpass
      password = getpass.getpass()
    if not options.file:
        parser.error('File path or url link is required to create a media to upload')

    with client(options.username, password) as cli:
        text = options.caption or ''
        cli.upload(options.file, text)

if __name__ == '__main__':
    main()
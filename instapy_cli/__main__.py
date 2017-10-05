import sys
import instapy_cli
from optparse import OptionParser


def main(args=None):
    """ The main routine """
    welcome_msg = 'instapy-cli ' + u'\ud83d\udd25'
    print(welcome_msg)
    if args is None:
        args = sys.argv[1:]
    parser = OptionParser(usage="usage: %prog [options]")
    parser.add_option('-u', dest='username', help='username')
    parser.add_option('-p', dest='password', help='password')
    parser.add_option('-f', dest='file', help='file path')
    parser.add_option('-t', dest='caption', help='caption text')

    (options, args) = parser.parse_args(args)
    if not options.username:
        parser.error('Username is required')
    password = options.password
    if not options.password:
      import getpass
      password = getpass.getpass()
    if not options.file:
        parser.error('File path is required')

    with instapy_cli.client(options.username, password) as client:
        text = options.caption or ''
        client.upload(options.file, text)

if __name__ == '__main__':
    main()
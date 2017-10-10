import sys
from platform import python_version
from instapy_cli.cli import InstapyCli as client
from optparse import OptionParser
from emoji import emojize


def main(args=None):

    welcome_msg = emojize(':laptop_computer:  instapy-cli :camera:')
    print(welcome_msg)
    print(emojize(':snake:  Python version: ' + python_version()))

    # cli = client()
    # cli.loop(args)

    if args is None:
        print('use >> instapy -u <USERNAME> -p <PASSWORD> -f <IMAGE.JPG> -t <CAPTION>')
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

    with client(options.username, password) as cli:
        text = options.caption or ''
        cli.upload(options.file, text)

if __name__ == '__main__':
    main()
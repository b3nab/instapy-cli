from instapy_cli import client

username = 'USERNAME'
password = 'PASSWORD'

with client(username, password) as cli:
    # do stuffs with cli
    ig = cli.api()
    print(ig.current_user())

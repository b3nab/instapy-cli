from instapy_cli import client

username = 'USERNAME'
password = 'PASSWORD'
cookie_file = 'COOKIE_FOR_USER.json' # default: `USERNAME_ig.json`

with client(username, password, cookie_file=cookie_file, write_cookie_file=True) as cli:
    # get string cookies
    cookies = cli.get_cookie()
    print(type(cookies)) # == str
    print(cookies)
    # do stuffs with cli
    ig = cli.api()
    me = ig.current_user()
    print(me)

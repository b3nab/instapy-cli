from instapy_cli import client

username = 'USERNAME'
password = 'PASSWORD'
cookie = '{COOKIE_STRING_JSON_OBJ}'

with client(username, password, cookie=cookie) as cli:
    # get string cookies
    cookies = cli.get_cookie()
    print(type(cookies)) # == str
    print(cookies)
    # do stuffs with cli
    ig = cli.api()
    me = ig.current_user()
    print(me)

from instapy_cli import client

username = 'USERNAME'
password = 'PASSWORD'

# There are two ways to use instapy-cli programmatically:
# vvv << see below >> vvv

# Create cli and use it in functions/classes/parameters
cli = client(username, password)
ig = cli.api()
me  = ig.current_user()
print(me)


# Create cli using 'with ... as ..' - a more pythonic way
with client(username, password) as cli:
    # do stuffs with cli
    ig = cli.api()
    me = ig.current_user()
    print(me)

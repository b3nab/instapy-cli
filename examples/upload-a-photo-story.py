from instapy_cli import client

username = 'USERNAME'
password = 'PASSWORD'
image = 'docs/image-sample-upload.jpg'

with client(username, password) as cli:
    cli.upload(image, story=True)

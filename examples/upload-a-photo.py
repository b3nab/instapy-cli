from instapy_cli import client

username = 'USERNAME'
password = 'PASSWORD'
image = 'docs/image-sample-upload.jpg'
text = 'This will be the caption of your photo.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

with client(username, password) as cli:
    cli.upload(image, text)

from instapy_cli import client

username = 'USERNAME'
password = 'PASSWORD'
video = 'docs/video-sample-upload.mp4'
text = 'This will be the caption of your video.' + '\r\n' + 'You can also use hashtags! #hash #tag #now'

with client(username, password) as cli:
    cli.upload(video, text)

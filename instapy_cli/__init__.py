from instapy_cli.cli import InstapyCli as cli


def client(*args, **kwargs):
    return cli(*args, **kwargs)
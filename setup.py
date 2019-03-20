import os
import codecs

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

def read(*parts):
    """
    Build an absolute path from *parts* and and return the contents of the
    resulting file.  Assume UTF-8 encoding.
    """
    with codecs.open(os.path.join(here, *parts), "rb", "utf-8") as f:
        return f.read()

setup(
    name='instapy-cli',
    version='0.0.7',
    description='Python library and cli used to upload photo on Instagram. W/o a phone!',
    long_description=read('README.rst'),
    classifiers=[
        # How mature is this project?
        'Development Status :: 5 - Production/Stable',

        # For who your project is intended for and its usage
        'Intended Audience :: Developers',
        'Environment :: Console',

        # Project's License
         'License :: OSI Approved :: MIT License',

        # Python versions instapy-cli support here
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    keywords='instagram private upload api instapy instapy-cli instapycli',
    author='Benedetto Abbenanti',
    author_email='benedetto.abbenanti@gmail.com',
    url='https://github.com/b3nab/instapy-cli',
    license='MIT',
    packages=['instapy_cli'],
    install_requires=[ # external packages as dependencies
        'requests>=2',
        'Pillow>=5.2.0',
        'instagram-private-api==1.6.0',
        'instagram-private-api_extensions==0.3.8',
    ],
    dependency_links=[
        'git+ssh://git@github.com/ping/instagram_private_api.git@1.6.0#egg=instagram_private_api-1.6.0',
        'git+https://git@github.com/ping/instagram_private_api_extensions.git@0.3.8#egg=instagram_private_api_extensions-0.3.8',
    ],
    entry_points={
        'console_scripts': [
            'instapy=instapy_cli.__main__:main'
        ]
    },
)

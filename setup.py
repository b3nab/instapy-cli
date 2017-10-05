import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='instapycli',
    version='0.0.1.dev1',
    description='Python library and cli used to upload photo on Instagram. W/o a phone!',
    long_description='',
    classifiers=[
        '',
    ],
    keywords='instagram private upload api',
    author='Benedetto Abbenanti',
    author_email='benedetto.abbenanti@gmail.com',
    url='https://github.com/b3nab/instapy-cli',
    license='MIT',
    packages=['instapy_cli'],
    install_requires=['requests>=2'], #external packages as dependencies
    entry_points={
        'console_scripts': [
            'instapy=instapy_cli.__main__:main'
        ]
    },
    # python_requires='>=2.7'
)
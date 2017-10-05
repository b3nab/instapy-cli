import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='instapy-cli',
    version='0.1dev-rc1',
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
    packages=['instapy-cli'],  #same as name
    install_requires=['bar', 'greek'], #external packages as dependencies
    entry_points={
        'console_script' = [
            'instapy=instapy-cli.instapy-cli:main'
        ]
    },
    python_requires='>=2.7'
)
import os

from setuptools import setup, find_packages

here = os.path.abspath(os.path.dirname(__file__))

setup(
    name='instapy-cli',
    version='0.0.1-dev0',
    description='Python library and cli used to upload photo on Instagram. W/o a phone!',
    long_description=open('README.md').read(),
    classifiers=[
        # How mature is this project? Common values are
        #   3 - Alpha
        #   4 - Beta
        #   5 - Production/Stable
        'Development Status :: 3 - Alpha',

        # Indicate who your project is intended for
        'Intended Audience :: Developers',
        # 'Topic :: Software Development :: Build Tools',

        # Pick your license as you wish (should match "license" above)
         'License :: OSI Approved :: MIT License',

        # Specify the Python versions you support here. In particular, ensure
        # that you indicate whether you support Python 2, Python 3 or both.
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
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
    install_requires=['requests>=2'], #external packages as dependencies
    entry_points={
        'console_scripts': [
            'instapy=instapy_cli.__main__:main'
        ]
    },
    # python_requires='>=2.7'
)
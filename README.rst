**instapy-cli**
=====================

|Instapy-Cli version| |MIT license|

Python library and cli used to upload photo on Instagram. W/o a phone!
You can upload a local file or use a link, it do all automagically.


.. image:: https://github.com/b3nab/instapy-cli/raw/master/docs/instagram-private-banner.png
   :width: 650px
   :align: center

--------------

Introduction
------------

There are a plenty of libraries written in Python dedicated to Instagram
APIs (public or ***private***, no matter).. but most of them have
unsolved issues and PR not maintained for a time as long as 5-6 months.

At the same time lots of developers want a simple and effective way to
post/\ **upload** an photo/\ **image** **programmatically**.

So I dedice to start this repo and OpenSource it w/ :heart:

***``[FUTURE] spoiler:``*** And if I want to upload a video?

Usage
~~~~~

**Install**

``pip install instapy-cli``

**Use**

``instapy -u USR -p PSW -f FILE/LINK -t 'TEXT CAPTION'``

**Help**

``instapy --help``

Why instapy-cli?
~~~~~~~~~~~~~~~~

First, long story short: instapy-cli is a fork of pynstagram, with the
aim of extend its functionality and fix all unresolved bug.

Move this project to a better place :arrow\_right\_hook:
''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Anyone that want to collaborate, I'll promise to be a good Repo Manager
and merge all yours Pull Request as soon as possible. I have some ideas
to improve this but I need collaboration. Enter and support! :bulb:

But, wait! Instagram don't let to upload a photo except from app ( of course :trollface: )
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

Short answer: > Yes, you are right.

Long answer: > Every connection from a mobile phone could be
intercepted. Someone has done the hard work to sniff the packets sended
from phone to Instagram and "spread the news". You could do a quick
research.

Code Requirements
-----------------

This packages will be installed automatically with *instapy-cli*

+------------+----------------------------------------+
| package    | Source Link                            |
+============+========================================+
| requests   | https://github.com/requests/requests   |
+------------+----------------------------------------+

License
-------

MIT

Contribute
----------

To help ``instapy-cli`` developers to build and maintain this project,
go to **`docs/CONTRIBUTING.md <https://github.com/b3nab/instapy-cli/blob/master/docs/CONTRIBUTING.md>`__** > instruction
soon

(Write it and collaborate! :wink:)

.. |Instapy-Cli version| image:: https://img.shields.io/pypi/v/instapy-cli.svg
   :target: https://pypi.org/project/instapy-cli
.. |MIT license| image:: https://img.shields.io/github/license/b3nab/instapy-cli.svg
   :target: https://github.com/b3nab/instapy-cli/blob/master/LICENSE

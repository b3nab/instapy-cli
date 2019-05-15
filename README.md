# **instapy-cli** :zap:

Publish *photos* and *videos* (NEW!) on Instagram, without a phone! You can upload **posts** and even **stories** on Instagram.
You can upload a local file or use a link, it does everything for you automagically.

<p align="center">
  <img src="https://raw.githubusercontent.com/instagrambot/instapy-cli/master/docs/instagram-private-banner.png" alt="instapy-cli instagram-private-api" width="650px">
</p>

---
[![Build Status](https://img.shields.io/badge/Paypal-DONATE-blue.svg?logo=paypal
)](https://paypal.me/b3nab)
[![instapy-cli version](https://img.shields.io/pypi/v/instapy-cli.svg)](https://pypi.org/project/instapy-cli)
[![Build Status](https://travis-ci.org/instagrambot/instapy-cli.svg?branch=master)](https://travis-ci.org/b3nab/instapy-cli)
[![MIT license](https://img.shields.io/github/license/instagrambot/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/blob/master/LICENSE)


[![GitHub issues](https://img.shields.io/github/issues/instagrambot/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/issues)
[![GitHub forks](https://img.shields.io/github/forks/instagrambot/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/network)
[![GitHub stars](https://img.shields.io/github/stars/instagrambot/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/stargazers)


## Introduction
There are plenty of libraries written in Python specialized on working on Instagram APIs (either public or private), but most of them have lots of unsolved issues and PRs not maintained for a long time.

> Lots of developers want a simple and effective way to upload photos or videos (NEW!) directly to Instagram **programmatically**. Some may want to publish a simple post, others want to publish a story.

All this can be achieved with `instapy-cli`. :tada:

I dedided to start this repo and open-source it with :heart:


### Installation

<!-- **Install** -->

```shell
pip install instapy-cli
```

### Usage

#### Use as Library

You can check the folder `examples` to see working codes to use instapy-cli programmatically.
If you want to use instapy-cli via shell continue reading.

#### Use as CLI

**Use**

```shell
instapy -u USR -p PSW -f FILE/LINK -t 'TEXT CAPTION'
```

**CLI Options**

| option | required | default | description |
| --- | --- | --- | --- |
| -u | **yes** | - | username |
| -p | **yes** | - | password |
| -f | **yes** | - | file/media to upload |
| -t | *optional* | - | text caption for post |
| -s | *optional* | - | upload a story |

**Help**

```shell
instapy --help
```


#### Hints
##### Cookie
You can avoid to re-login, by using a cookie that instapy-cli generate for you.
By default instapy-cli use the cookie created in current working directory with the name 'USERNAME_ig.json'.
If you don't want to store the cookie in your filesystem you need to pass the parameter `cookie`:

```python
with client(username, password, cookie) as cli:
    # do stuffs with cli
```

This is feature is not well tested, be carefull using it.

##### Image Format
instapy-cli support images in the format of JPG/JPEG/PNG.

##### Aspect Ratio
The images need to have an aspect ratio of 1:1, that is squared size.
You can use other aspect-ratio other than 1:1, but be carefull to stay inside Instagram limits.
Otherwise, if you don't respect the aspect ratio, the media will be posted but stretched or cropped.

### Why instapy-cli?
First, long story short: instapy-cli is a fork of pynstagram, with the aim of extending its functionality and fixing all unresolved bugs.

##### Move this project to a better place :arrow_right_hook:
Anyone that wants to collaborate, I promise to be a good repo manager and merge all your pull requests as soon as possible.
I have some ideas to improve this but I need collaboration. Join and support! :bulb:

##### But, wait! Instagram doesn't allow uploading content except from the app (of course :trollface:)
Short answer:
> Yes, you are right.

Long answer:
> Every connection from a mobile phone could be intercepted. Someone has done the hard work to sniff the packets sent from the phone to Instagram and "spread the news". You can do a quick research.

## Code Requirements
#### This packages will be installed automatically with *instapy-cli*

| package     | Source Link |
| :---:       | :---: |
| requests    | https://github.com/requests/requests |
| filetype    | https://github.com/h2non/filetype.py |
| instagram-private-api    | https://github.com/ping/instagram_private_api |
| instagram-private-api-extensions    | https://github.com/ping/instagram_private_api_extensions |

## Contribute
To help `instapy-cli` developers to build and maintain this project, go to **[docs/CONTRIBUTING.md](/docs/CONTRIBUTING.md)**
> instructions soon

(Write it and collaborate! :wink:)

## License
MIT

## Support the project and the author
Offer me a coffe or a beer and support instapy-cli. :tada:

Click the button here >
[![Build Status](https://img.shields.io/badge/Paypal-DONATE-blue.svg?logo=paypal
)](https://paypal.me/b3nab)

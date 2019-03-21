# **instapy-cli** :zap:

[![Build Status](https://img.shields.io/badge/Paypal-DONATE-blue.svg?logo=paypal
)](https://paypal.me/b3nab)
####
[![instapy-cli version](https://img.shields.io/pypi/v/instapy-cli.svg)](https://pypi.org/project/instapy-cli)
[![Build Status](https://travis-ci.org/b3nab/instapy-cli.svg?branch=master)](https://travis-ci.org/b3nab/instapy-cli)
[![MIT license](https://img.shields.io/github/license/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/blob/master/LICENSE)

###### *Repo Infos*
[![GitHub issues](https://img.shields.io/github/issues/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/issues)
[![GitHub forks](https://img.shields.io/github/forks/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/network)
[![GitHub stars](https://img.shields.io/github/stars/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/stargazers)

---

Python library and cli used to post photos and videos (NEW!) on Instagram, without a phone!
You can upload a local file or use a link, it does everything automagically.

<p align="center">
  <img src="https://raw.githubusercontent.com/b3nab/instapy-cli/master/docs/instagram-private-banner.png" alt="instapy-cli instagram-private-api" width="650px">
</p>

---

## Introduction
There are plenty of libraries written in Python specialized on working on Instagram APIs (either public or private), but most of them have unsolved issues and PRs not maintained for a time as long as 5-6 months.

At the same time, lots of developers want a simple and effective way to post photos or videos (NEW!) **programmatically**.

So I dedided to start this repo and open-source it with :heart:


### Install

**Install**

```shell
pip install instapy-cli
```

### Use as Library

You can check the folder `examples` to see working codes to use instapy-cli programmatically.
If you want to use instapy-cli via shell continue reading.

### Use as CLI

**Use**

```shell
instapy -u USR -p PSW -f FILE/LINK -t 'TEXT CAPTION'
```

**Help**

```shell
instapy --help
```


#### Hint
*Image Format*
Instapy-cli support images in the format of JPG/JPEG/PNG.

*Aspect Ratio*
The images need to have an aspect ratio of 1:1, that is squared size.
You can use other aspect-ratio other than 1:1, but be carefull to stay inside this limits:
- MIN_ASPECT_RATIO = 0.80
- MAX_ASPECT_RATIO = 1.91
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
| instagram-private-api    | https://github.com/ping/instagram_private_api |
| instagram-private-api-extensions    | https://github.com/ping/instagram_private_api_extensions |

## License
MIT

## Contribute
To help `instapy-cli` developers to build and maintain this project, go to **[docs/CONTRIBUTING.md](/docs/CONTRIBUTING.md)**
> instructions soon

(Write it and collaborate! :wink:)

## Support the project and the author
Offer me a coffe or a beer and support instapy-cli. :tada:

Click the button here >
[![Build Status](https://img.shields.io/badge/Paypal-DONATE-blue.svg?logo=paypal
)](https://paypal.me/b3nab)

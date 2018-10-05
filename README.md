# **instapy-cli** :zap:

[![Build Status](https://travis-ci.org/b3nab/instapy-cli.svg?branch=master)](https://travis-ci.org/b3nab/instapy-cli)
[![instapy-cli version](https://img.shields.io/pypi/v/instapy-cli.svg)](https://pypi.org/project/instapy-cli)
[![MIT license](https://img.shields.io/github/license/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/blob/master/LICENSE)

###### *Github Infos*
[![GitHub issues](https://img.shields.io/github/issues/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/issues)
[![GitHub forks](https://img.shields.io/github/forks/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/network)
[![GitHub stars](https://img.shields.io/github/stars/b3nab/instapy-cli.svg)](https://github.com/b3nab/instapy-cli/stargazers)

---

Python library and cli used to post photos on Instagram, without a phone!
You can upload a local file or use a link, it does everything automagically.

<p align="center">
  <img src="docs/instagram-private-banner.png" alt="instagram-private-api" width="650px">
</p>

---

## Introduction
There are plenty of libraries written in Python dedicated to Instagram APIs (either public or private).. but most of them have unsolved issues and PRs not maintained for a time as long as 5-6 months.

At the same time, lots of developers want a simple and effective way to post photos **programmatically**.

So I dediced to start this repo and open-source it with :heart:


***`[FUTURE] spoiler:`*** And what if I want to upload a video?


### Usage

**Install**

`pip install instapy-cli`

**Use**

`instapy -u USR -p PSW -f FILE/LINK -t 'TEXT CAPTION'`

**Help**

`instapy --help`

### Why instapy-cli?
First, long story short: instapy-cli is a fork of pynstagram, with the aim of extending its functionality and fixing all unresolved bugs.

##### Move this project to a better place :arrow_right_hook:
Anyone that wants to collaborate, I promise to be a good repo manager and merge all your pull requests as soon as possible.
I have some ideas to improve this but I need collaboration. Join and support! :bulb:

##### But, wait! Instagram doesn't allow uploading photos except from the app (of course :trollface:)
Short answer:
> Yes, you are right.

Long answer:
> Every connection from a mobile phone could be intercepted. Someone has done the hard work to sniff the packets sent from the phone to Instagram and "spread the news". You can do a quick research.

## Code Requirements
#### This packages will be installed automatically with *instapy-cli*

| package     | Source Link |
| :---:       | :---: |
| requests    | https://github.com/requests/requests |

## License
MIT

## Contribute
To help `instapy-cli` developers to build and maintain this project, go to **[docs/CONTRIBUTING.md](/docs/CONTRIBUTING.md)**
> instructions soon

(Write it and collaborate! :wink:)

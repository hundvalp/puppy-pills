# ![](https://raw.githubusercontent.com/hundvalp/puppy-pills/master/icon.png) Puppy Pills

[![Build Status][build-badge]][build-link] [![Coverage][coverage-badge]][coverage-link] [![MIT License][license-badge]](LICENSE.md)

Twitter bot for reminding a very special puppy of her meds :purple_heart:

## Usage

This bot tweets a randomly chosen reminder message when run. You'll need to run it with a scheduler to have it tweet regularly. Python 3 is supported, with no plans for Python 2 support.

Install the dependencies:

    pip install -r requirements.txt

Configure her by copying `config-sample.py` to `config.py` and tweaking it. You can add your own reminder messages and set which users the bot will mention when tweeting.

[coverage-badge]: https://codecov.io/gh/hundvalp/puppy-pills/branch/master/graph/badge.svg
[coverage-link]:  https://codecov.io/gh/hundvalp/puppy-pills
[license-badge]:  https://img.shields.io/badge/license-MIT-007EC7.svg
[build-badge]:    https://travis-ci.org/hundvalp/puppy-pills.svg?branch=master
[build-link]:     https://travis-ci.org/hundvalp/puppy-pills

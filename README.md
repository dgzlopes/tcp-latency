# tcp-latency
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tcp-latency.svg)](https://pypi.org/project/tcp-latency/)
[![PyPI](https://img.shields.io/pypi/v/tcp-latency.svg)](https://pypi.org/project/tcp-latency/)
[![PyPI - License](https://img.shields.io/pypi/l/tcp-latency.svg)](https://github.com/dgzlopes/tcp-latency/blob/master/LICENSE.md)
[![Build Status](https://travis-ci.org/dgzlopes/tcp-latency.svg?branch=master)](https://travis-ci.org/dgzlopes/tcp-latency)
[![PyPI - Downloads](https://img.shields.io/pypi/dm/tcp-latency)](https://pypistats.org/packages/tcp-latency)
## About
`tcp-latency` provides an easy way to measure latency using TCP.

Inspired by other [similar tools](#similar-tools), `tcp-latency` comes from the need of running network diagnosis/troubleshooting tasks with Python on serverless infrastructure (as many providers don't include ping/ICMP support) but should work too in any other environment with Python>=36.
## Features
- Runs as a command-line tool or inside your code as a module.
- Custom parameters for a port, runs, timeout and wait time between runs.
- IPv4 (e.g 52.26.14.11) and domain (e.g google.com) host support.
- Human readable output when running as a command-line tool.
- No external dependencies.
- Small and extensible.
## Usage
`tcp-latency` can be used both as a module and as a standalone script.

### Module
```
>>> from tcp_latency import measure_latency
>>> measure_latency(host='google.com')
[34.57]
>>> measure_latency(host='52.26.14.11', port=80, runs=10, timeout=2.5)
[433.82, 409.21, 409.25, 307.09, 306.64, 409.45, 306.58, 306.93, 409.25, 409.26]
```
Note: If omitted, `measure_latency()` arguments use the same defaults that command-line mode.
### Command-line
```
$ tcplatency -h
usage: tcp-latency [-h] [-p [p]] [-t [t]] [-r [r]] [-w [w]] h

Measure latency using TCP.

positional arguments:
  host

optional arguments:
  -h, --help            show this help message and exit
  -p [p], --port [p]    (default: 443)
  -t [t], --timeout [t]
                        (seconds, float, default: 5)
  -r [r], --runs [r]    number of latency points (int, default: 5)
  -w [w], --wait [w]    between each run (seconds, float, default: 1)
```
```
$ tcp-latency google.com
tcp-latency google.com
google.com: tcp seq=0 port=443 timeout=5 time=15.16 ms
google.com: tcp seq=1 port=443 timeout=5 time=15.63 ms
google.com: tcp seq=2 port=443 timeout=5 time=14.86 ms
google.com: tcp seq=3 port=443 timeout=5 time=14.76 ms
google.com: tcp seq=4 port=443 timeout=5 time=14.59 ms
--- google.com tcp-latency statistics ---
5 packets transmitted
rtt min/avg/max = 14.76/15.1025/15.63 ms

$ tcp-latency 52.26.14.11 --port 80 --runs 3 --wait 0.5
tcp-latency 52.26.14.11
52.26.14.11: tcp seq=0 port=80 timeout=5 time=230.2 ms
52.26.14.11: tcp seq=1 port=80 timeout=5 time=228.96 ms
52.26.14.11: tcp seq=2 port=80 timeout=5 time=224.51 ms
--- 52.26.14.11 tcp-latency statistics ---
3 packets transmitted
rtt min/avg/max = 228.96/229.57999999999998/230.2 ms

$ tcp-latency google.com -r 1
tcp-latency google.com
google.com: tcp seq=0 port=443 timeout=5 time=34.36 ms
--- google.com tcp-latency statistics ---
1 packets transmitted
```

## Installation
Via pip:
```
pip install tcp-latency
```
## How to contribute
1. Check for open issues or open a fresh issue to start a discussion around a feature idea or a bug.
2. Fork [the repository](https://github.com/dgzlopes/tcp-latency) on GitHub to start making your changes to the master branch (or branch off of it).
3. Write a test which shows that the bug was fixed or that the feature works as expected.
4. Send a [pull request](https://help.github.com/en/articles/creating-a-pull-request-from-a-fork) and bug [me](https://github.com/dgzlopes) until it gets merged and published.

Some things that would be great to have:
- Add transmitted vs received statistics (e.g packet loss)
- Add bytes information (ping-like)
- Add support for machine-readable output (JSON,XML,YAML).
- Add automated releases with TravisCI.
- Improve test suite.
- Improve `How to contribute` information (pyenv, tox, pre-commit...)

## Similar tools
- [yantisj/tcpping](https://github.com/yantisj/tcpping)
- [ipv6freely/tcpping](https://github.com/ipv6freely/tcpping)
- [yahoo/serviceping](https://github.com/yahoo/serviceping)

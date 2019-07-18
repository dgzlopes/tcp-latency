# tcp-latency
![PyPI - Python Version](https://img.shields.io/pypi/pyversions/tcp-latency.svg)
![PyPI](https://img.shields.io/pypi/v/tcp-latency.svg)
![PyPI - License](https://img.shields.io/pypi/l/tcp-latency.svg)
## About
`tcp-latency` provides an easy way to measure latency using TCP.

Inspired by other [similar tools](#similar-tools), `tcp-latency` comes from the need of running network diagnosis/troubleshooting tasks with Python on serverless infraestructure (as many providers don't include ping/ICMP support) but should work too in any other enviroment with Python>=36.
## Features
- Runs as command line tool or inside your code as a module.
- Custom parameters for port, runs, timeout and wait time between runs.
- IPv4 (e.g 52.26.14.11) and domain (e.g google.com) host support.
- Human readable output when runned as command line tool.
- Small and extensible.
## Usage
`tcp-latency` can be used both as a module and as an standalone script.

### Module
```
>>> from tcp_latency import meassure_latency
>>> meassure_latency(host='google.com')
[34.57]
>>> meassure_latency(host='52.26.14.11', port=80, runs=10, timeout=2.5)
[433.82, 409.21, 409.25, 307.09, 306.64, 409.45, 306.58, 306.93, 409.25, 409.26]
```
Note: If ommited, `meassure_latency()` arguments use the same defaults that command line mode.
### Command line
```
$ tcplatency -h
usage: tcp-latency [-h] [-p [p]] [-t [t]] [-r [r]] [-w [w]] h

Meassure latency using TCP.

positional arguments:
  host

optional arguments:
  -h, --help            show this help message and exit
  -p [p], --port [p]    (default: 443)
  -t [t], --timeout [t]
                        (seconds, float, default: 5)
  -r [r], --runs [r]    number of latency points (int, default: 5)
  -w [w], --wait [w]    between each run (seconds, float, default: 0)
```
```
$ tcplatency google.com
google.com: tcp seq=0 port=443 timeout=5 time=32.91 ms
google.com: tcp seq=1 port=443 timeout=5 time=14.1 ms
google.com: tcp seq=2 port=443 timeout=5 time=16.26 ms
google.com: tcp seq=3 port=443 timeout=5 time=16.35 ms
google.com: tcp seq=4 port=443 timeout=5 time=15.63 ms

$ tcplatency 52.26.14.11 --port 80 --runs 3 --wait 0.5
52.26.14.11: tcp seq=0 port=80 timeout=5 time=269.45 ms
52.26.14.11: tcp seq=1 port=80 timeout=5 time=409.2 ms
52.26.14.11: tcp seq=2 port=80 timeout=5 time=409.14 ms

$ tcp-latency google.com -r 1
google.com: tcp seq=0 port=443 timeout=5 time=34.36 ms
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
- Add at the end of human_output stadistics (ping-like).
- Add documentation (Sphinx?).
- Add Ipv6 support.
- Add support for machine readable output (json?xml?).
- Add automated testing and releases with CircleCI.
- Add codecov.
- Add to README.md a list of alternatives to tcp-latency.
- Improve formatting in human_output to feel more like ping.
- Improve test suite.
- Improve `How to contribute` information (pyenv, tox, pre-commit...)

## Similar tools
- [yantisj/tcpping](https://github.com/yantisj/tcpping)
- [ipv6freely/tcpping](https://github.com/ipv6freely/tcpping)
- [yahoo/serviceping](https://github.com/yantisj/tcpping)

performance
===========
[![Build Status](https://travis-ci.org/dmytrobondarchuk/performance.svg?branch=master)](https://travis-ci.org/dmytrobondarchuk/performance)
    
Performance testing tool for web applications

Requirements
------------
1. Python 3.5+
2. PyTest >= 3.2 (will be installed)
3. Requests >= 2.18 (will be installed)


Installation
------------
**Virtual environment** (recommended):

1. `git clone https://github.com/dmytrobondarchuk/performance.git`
2. `cd performance`
3. `python3 -m venv env`
4. `source env/bin/activate`
5. `pip install -r requirements.txt`

Usage
-----
**Virtual environment:**
1. ```cd performance```
2. ```source env/bin/activate```
3. ```python performance.py [-h] [--url [URL [URL ...]]] [--file [FILE [FILE ...]]] [--dir [DIR [DIR ...]]]```


_optional arguments:_
  - `-h, --help `
                        _show the help message and exit_
  - `--url [URL [URL ...]]`
                        _url of the page_
  - `--file [FILE [FILE ...]]`
                        _path to file with urls_
  - `--dir [DIR [DIR ...]]`
                        _path to the dir with text files with urls_


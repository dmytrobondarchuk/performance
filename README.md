performance
===========
[![Build Status](https://travis-ci.org/dmytrobondarchuk/performance.svg?branch=master)](https://travis-ci.org/dmytrobondarchuk/performance)
    
Performance testing tool for web applications (vers. 0.2.2)

Installation
------------
**Virtual environment** (recommended):



1. It requires Python 3.5+.
2. git clone https://github.com/dmytrobondarchuk/performance.git
3. cd performance
4. python3 -m venv env
5. source env/bin/activate
6. pip install -r requirements.txt

Usage
-----
**Virtual environment:**
1. cd performance
2. source env/bin/activate
3. python performance.py [-h] 
                      [--urls [URL [URLS ...]]]
                      [--file [FILE [FILE ...]]]
                      [--dir [DIR [DIR ...]]]
                      
_optional arguments:_
  - -h, --help 
                        _show the help message and exit_
  - --url [URL [URL ...]]
                        _url of the page_
  - --file [FILE [FILE ...]]
                        _path to file with urls_
  - --dir [DIR [DIR ...]]
                        _path to the dir with text files with urls_


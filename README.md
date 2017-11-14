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
  show the help message and exit
  - --urls [URLS [URLS ...]]
                        Urls directly passed from terminal
  - --file [FILE [FILE ...]]
                        Path to files with urls.
  - --dir [DIR [DIR ...]]
                        Paths to the dirs with text files with urls.


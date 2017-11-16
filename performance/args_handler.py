# -*- coding: utf-8 -*-
"""Tool for web-application performance analysis. It's based on Google's PageSpeed."""


import argparse
from .urls_handler import get_urls_from_file
from .urls_handler import get_urls_from_dir
from .testing import testing
from .testing import message


def main(args):
    """Handle args and run testing"""
    if (args.file, args.url, args.dir).count(None) == 3:
        print("No urls. Please retry. Use [-h, --help] for help")
    else:
        print(message['test_results'])

    if args.file is not None:
        if len(args.file) == 0:
            testing(get_urls_from_file('file_with_urls.txt'))
        else:
            testing(get_urls_from_file(args.file))

    if args.url is not None:
        if len(args.url) == 0:
            print("No urls")
        else:
            testing(args.url)

    if args.dir is not None:
        if len(args.dir) == 0:
            testing(get_urls_from_dir('urls'))
        else:
            testing(get_urls_from_dir(args.dir))




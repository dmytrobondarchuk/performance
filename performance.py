# -*- coding: utf-8 -*-
"""Tool for web-application performance analysis. It's based on Google's PageSpeed."""

from performance.args_handler import main
import argparse


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='User database utility')
    parser.add_argument('--url', nargs='*', help='Url of the page test '
                                                 '(Example:  --url https://url1.com https://url2.org ...)', )
    parser.add_argument('--file', nargs='*', help='Path to file with urls. '
                                                  '(Example: --file /abs_path/to/the/dir/file.txt  '
                                                  'relative/to/performance/file.txt)', )
    parser.add_argument('--dir', nargs='*', help='Path to the dir with text files with urls.'
                                                 'Example:  --dir /abs/path/to/dir_with_files '
                                                 'path/relative/to/performance/dir_with_files', )
    parser.set_defaults(func=main)
    passed_args = parser.parse_args()
    passed_args.func(passed_args)


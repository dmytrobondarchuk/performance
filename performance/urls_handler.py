# -*- coding: utf-8 -*-
"""Tool for web-application performance analysis. It's based on Google's PageSpeed."""


import os


message = {'no_urls': "We need an URL of the page to test,\n" +
                      "for example 'https://example.com'.\n\n" +
                      "Also there can be multiple urls, separated by comma,\n" +
                      "for example: https://example1.com https://example2.com https://example3.com\n\n" +
                      "Also urls of the page can be read from the file 'file_with_urls.txt'"
                      "Please, retry ...",
           'using_urls_from_file': "We've got urls from the file 'file_with_urls.txt'",
           'test_results': "\n{:-^80}\n".format(" Results of performance testing "),
           }


def get_urls_from_file(files_with_urls):
    """
    Gets urls of pages to test their performance
    :param files_with_urls: default path to the file with urls or list of ones
    :return: list of urls
    """
    urls = []

    if type(files_with_urls) == str:
        with open(files_with_urls, 'r', encoding='utf-8') as f:
            for line in f:
                if 'http' in line[:4]:
                    if '\n' in line:
                        urls.append(line[:-1])
                    else:
                        urls.append(line)
    else:
        for text_file in files_with_urls:
            with open(text_file, 'r', encoding='utf-8') as f:
                for line in f:
                    if 'http' in line[:4]:
                        if '\n' in line:
                            urls.append(line[:-1])
                        else:
                            urls.append(line)
    return urls


def get_urls_from_dir(folder):
    """
    Gets urls of pages from files located in the folder to test performance of these pages.
    :param folder: default paths to the folders with files which contain urls
    :return: list of urls
    """
    folders = []
    urls = []
    if type(folder) == str:
        folders.append(folder)
    else:
        folders = folder

    for i in folders:
        if os.path.isdir(i):
            for text_file in os.listdir(i):
                for each_url in (get_urls_from_file(os.path.join(os.getcwd(), i,  text_file))):
                    urls.append(each_url)
        else:
            print("No such directory")
    return urls

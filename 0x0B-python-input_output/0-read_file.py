#!/usr/bin/python3
'''this module contains the read_file function'''


def read_file(filename=""):
    '''
    function that reads a text file (UTF8)
    and prints it to stdout
    '''
    with open(filename, encoding="utf-8") as f:
        for line in f:
            print(f.read(), end="")

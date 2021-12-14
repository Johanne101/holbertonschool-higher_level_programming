#!/usr/bin/python3
'''Module: append_write function'''


def append_write(filename='', text=''):
    '''
    Appends string at the end of text file
    and returns the number of characters added
    '''
    with open(filename, 'a', encoding='utf-8') as f:
        return f.write(text)

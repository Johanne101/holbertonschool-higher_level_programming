#!/usr/bin/python3
'''
Module contains "is same class(obj,a_class)" function
'''


def is_same_class(obj, a_class):
    """ function returns:
    True: if the object is exactly an instance of the specified class.
    or
    False: otherwise.
    """
    if type(obj) is a_class:
        return True
    else:
        return False

#!/usr/bin/python3
'''
Module contains "is same class(obj,a_class)" function
'''


def is_kind_of_class(obj, a_class):
    """ function returns,
    If is an instance of object or,
    an instance of a class,
    inherited from the specified class:
    True or False: if instance object
    or
    True or False: if instance class.
    """
    if isinstance(obj, a_class):
        return True
    else:
        return False

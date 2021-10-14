#!/usr/bin/python3
'''
Module contains "inherits_from(obj, a_class)" function
'''


def inherits_from(obj, a_class):
    """ function returns,
    If is an instance of object or,
    an instance of a class,
    inherited from the specified class:
    True or False: if instance object
    or
    True or False: if instance class.
    """
    return type(obj) != a_class and issubclass(type(obj), a_class)

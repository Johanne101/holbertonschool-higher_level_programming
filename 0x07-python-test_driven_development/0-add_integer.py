#!/usr/bin/python3
"""Documentation of a add two integers function"""


def add_integer(a, b=98):

    """
    Adds two integers.
        Arguments:
        a (int): First number to add.
        b (int): Second number to add 'a' by.
        Return: The product of a and b
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    '''
        a = int(a)
        b = int(b)
    '''
    return (int(a) + int(b))

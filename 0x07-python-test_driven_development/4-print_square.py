#!/usr/bin/python3
"""Print square module"""


def print_square(size):
    """
    Print a square based on the size
    """
    if size < 0:
        raise ValueError("size must be >= 0")
    if type(size) is not int:
        raise TypeError("size must be an integer")

    for row in range(size):
        print("#" * size)

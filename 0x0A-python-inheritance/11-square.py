#!/usr/bin/python3
"""Task: Square #2"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    class Square inherits from Rectangle
    """
    def __init__(self, size):
        """
        Initialize Square object
        """
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

    def __str__(self):
        """
        __str__ representation of square
        """
        return "[Square] {}/{}".format(self.__size, self.__size)

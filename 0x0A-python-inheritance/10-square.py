#!/usr/bin/python3
"""module: Square #1"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """A square that inherits from a Rectangle
    """
    def __init__(self, size):
        """Initializes Square Class"""
        self.integer_validator("size", size)
        Rectangle.__init__(self, size, size)
        self.__size = size

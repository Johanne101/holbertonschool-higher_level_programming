#!/usr/bin/python3
"""1. Create a class called 'Square' (module)"""


class Square:
    """2. Ceating a defined Square class"""

    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        return self.__size

    @size.setter
    def size(self, value):
        """setter function of size"""
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = value

    def area(self):
        """ area of square"""
        return self.__size**2

    def my_print(self):
        if self.size == 0:
            print()
        for row in range(self.__size):
            for col in range(self.size):
                print('#', end="")
            print()

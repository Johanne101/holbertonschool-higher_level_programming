#!/usr/bin/python3
""" Rectangle Class defining a rectangle
"""


class Rectangle:
    """ Create a method defined 'Rectangle'
        data type attributes:
            width: to be retrieved, and must be an {int}
            height: to be retrieved, and must be an {int}
    """
    def __init__(self, width=0, height=0):
        self.__height = height
        self.__width = width

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        """ Property to set value
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            return ((self.__height + self.__width) * 2)

    def __str__(self):
        """ The method will print the rectangle
            with # character
        """
        my_object = ""
        if self.height == 0 or self.width == 0:
            return (my_object)
        for y in range(self.__height):
            for x in range(self.__width):
                my_object += "#"
            my_object += "\n"
        return my_object[:-1]

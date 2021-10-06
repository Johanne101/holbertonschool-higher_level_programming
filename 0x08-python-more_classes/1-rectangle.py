#!/usr/bin/python3
"""
Here is a module definin a Rectangle Class.

"""


class Rectangle:
    """
    Class 'Rectangle'
    data type attributes:

        width: to be retrieved, and must be an {int}
        height: to be retrieved, and must be an {int}
    """

    def __init__(self, width=0, height=0):
        """
        Initialization method for rectangle object's attributes.
        param:
            width: width value of rectangle.
            height: height value of rectangle.

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """
        Getter method.
        Private instance attribute.

        """
        return self.__width

    @width.setter
    def width(self, value):
        """
        Property to set width value.

        param:
        value: value to set width
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
        Getter method for height.

        Private height attribute.
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
        Property to set height.

        param:
            value: value to set height.

        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

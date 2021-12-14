#!/usr/bin/python3
"""Task: Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class that inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Instantiation with:
            - width
            - height
        """
        BaseGeometry.integer_validator(self, 'height', height)
        BaseGeometry.integer_validator(self, 'width', width)
        self.__height = height
        self.__width = width

    def area(self):
        """method"""
        return self.__height * self.__width

    def __str__(self):
        """
        String represenation returns,
        the following rectangle description
        """
        return "[Rectangle] {}/{}".format(self.__width, self.__height)

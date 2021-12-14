#!/usr/bin/python3
"""Task: Rectangle
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Clas inherits from BaseGeometry"""
    def __init__(self, width, height):
        """Initialize instance"""
        BaseGeometry.integer_validator(self, 'width', width)
        BaseGeometry.integer_validator(self, 'height', height)
        self.__width = width
        self.__height = height

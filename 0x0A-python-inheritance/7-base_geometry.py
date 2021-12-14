#!/usr/bin/python3
"""Module: BaseGeometry class"""


class BaseGeometry():
    """Base Class"""
    def area(self):
        """Method for area description"""
        raise Exception('area() is not implemented')

    def integer_validator(self, name, value):
        """Method validates 'value'"""
        if type(value) != int:
            raise TypeError("{} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(name))

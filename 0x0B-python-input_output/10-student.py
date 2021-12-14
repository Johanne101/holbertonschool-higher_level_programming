#!/usr/bin/python3
'''Module: student module to JSON Filter function'''


class Student:
    '''Student class Attributes:
        first_name(str), last_name(str) and age(int)'''
    def __init__(self, first_name, last_name, age):
        '''initialize objects'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        '''
        Retrieves a dictionary representation of Student instance.
        - if attrs is a list of strings, only attribute names
        contained in this list must be retrieved.
        - Otherwise, all attributes must be retrieved
        '''
        if attrs is None:
            return self.__dict__
        adict = {}
        for key, value in self.__dict__.items():
            if key in attrs:
                adict[key] = value
        return adict

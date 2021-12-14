#!/usr/bin/python3
'''module that contains student module'''


class Student:
    '''student class Attributes:
        first_name(str), last_name(str) and age(int)'''
    def __init__(self, first_name, last_name, age):
        '''initialize objects'''
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        '''Public method
        retrieves a dictionary representation of student instance
        '''
        return self.__dict__

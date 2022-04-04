#!/usr/bin/python3
'''
Module contains a class called "MyList(list)"
and all its methods and attributes.
'''


class MyList(list):
    """ Class inherits from the class "list"
    with a method that prints a sorted list.
    """
    def print_sorted(self):
        """
        Prints a sorted list
        """
        copy_list = self.copy()
        copy_list.sort()
        """
        """
        print(copy_list)

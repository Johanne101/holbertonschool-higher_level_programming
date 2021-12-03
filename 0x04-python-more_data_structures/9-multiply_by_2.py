#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    d_dictionary = {}
    for key, value in a_dictionary.items():
        d_dictionary[key] = value * 2

    return d_dictionary

#!/usr/bin/python3


def no_c(my_string):
    no_c = my_string
    new_string = no_c.translate({ord('C'): None})
    return (new_string)

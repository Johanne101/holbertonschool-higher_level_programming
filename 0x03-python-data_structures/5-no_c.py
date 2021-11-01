#!/usr/bin/python3


def no_c(my_string):
    new_string = my_string.translate({ord(ctr): None for ctr in 'cC'})
    return(new_string)

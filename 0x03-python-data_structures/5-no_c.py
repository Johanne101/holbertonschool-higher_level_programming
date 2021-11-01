#!/usr/bin/python3


def no_c(my_string):
    no_c = my_string
    new_string = no_c.translate({ord(ctr): None for ctr in 'cC'})
    return(new_string)

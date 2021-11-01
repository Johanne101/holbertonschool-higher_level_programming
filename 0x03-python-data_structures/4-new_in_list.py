#!/usr/bin/python3


def new_in_list(my_list, idx, element):
    if idx < 0 or idx > len(my_list) - 1:
        return (my_list)
    else:
        copy_l = my_list.copy()
        copy_l[idx] = element
        return (copy_l)

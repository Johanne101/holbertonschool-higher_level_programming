#!/usr/bin/python3


def delete_at(my_list=[], idx=0):
    """
    Function deletes an item at a
    specific position in a list.

    idx: index is position in list to delete.
    my_list: list of items/int's to verify.

    -If idx is negative or out of range,
    nothing change (returns the same list)
    """
    if idx < 0 or idx >= len(my_list):
        return my_list

    else:
        del(my_list[idx])
        return my_list

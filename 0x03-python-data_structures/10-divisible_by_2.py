#!/usr/bin/python3


def divisible_by_2(my_list=[]):
    """
    Function finds all numbers ("n")
    multiples of 2 in a list (my_list),
    using mul_of_2_lst variable to confirm
    if TRUE or FALSE.
    """
    if len(my_list) > 0:

        mult_of_2_lst = []

        for n in my_list:
            if n % 2 == 0:
                mult_of_2_lst.append(True)
            else:
                mult_of_2_lst.append(False)

        return mult_of_2_lst

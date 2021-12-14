#!/usr/bin/python3
"""Module: pascal_triangle function"""


def pascal_triangle(n):
    '''Returns a list of lists of integers
    representing the Pascal’s triangle of `n`
    '''
    if n < 1:
        return []

    '''container to collect the rows '''
    pascal_list = []
    l_list = [1]
    for item in range(n):
        pascal_list.append(l_list)
        r_list = l_list[:] + [0]
        i = 1
        for j in l_list:
            r_list[i] += j
            i += 1
        l_list = r_list
    return pascal_list

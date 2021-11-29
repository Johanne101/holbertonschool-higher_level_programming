#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for item in matrix:
        for num in item:
           print("{:d}".format(num), end='')
           if num != item[-1]:
               print(" ", end='')
        print()

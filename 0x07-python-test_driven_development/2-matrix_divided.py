#!/usr/bin/python3
"""Function that divides the elements of a matrix"""


def matrix_divided(matrix, div):
    """Prototype: def matrix_divided(matrix, div):
    * Matrix must be a  list of lists of integers/floats"
       - otherwise raise a TypeError exception with the message:

    * Each row of the matrix must be of the same size,
        - otherwise raise a TypeError exception with the message:
    * div must be a number (integer or float),
        - otherwise raise a TypeError exception with the message:
        - "div must be a number"
    * div can’t be equal to 0,
        - otherwise raise ZeroDivisionError exception with the message:
        - "division by zero"
    * Returns: a new matrix

        Arguments:
        matrix (list of lists): matrix to divide
        div (int or float): number to divide the matrix
    """
    Notlst = 'matrix must be a matrix (list of lists) of integers/floats'
    NotSize = 'Each row of the matrix must have the same size'

    if not isinstance(matrix, list):
        raise TypeError(Notlst)

    if not isinstance(div, (int, float)):
        raise TypeError('div must be a number')

    if div == 0:
        raise ZeroDivisionError('division by zero')

    xPos = len(matrix[0])

    for row in matrix:
        if xPos != len(row):
            raise TypeError(NotSize)

    for row in matrix:
        if len(row) == 0:
            raise TypeError(Notlst)
        if not isinstance(row, list):
            raise TypeError(Notlst)
        for value in row:
            if not isinstance(value, (int, float)):
                raise TypeError(Notlst)

    return [[round(value / div, 2) for value in row] for row in matrix]

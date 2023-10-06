#!/usr/bin/python3
"""An ALx module for TDD task 1"""


def matrix_divided(matrix, div):
    """Divides all Elements of matrix by div"""
    if not isinstance(matrix, list):
        raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")

    my_len = None
    # get main size of row
    if len(matrix) > 0 and type(matrix[0]) is list:
        my_len = len(matrix[0])
    # check that matrix is a list of
    if any(not isinstance(i, list) for i in matrix):
        raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")

    for lists in matrix:
        if any(type(x) not in [int, float] for x in lists):
            raise TypeError("matrix must be a matrix (list of \
lists) of integers/floats")

    if any(len(i) != my_len for i in matrix):
        raise TypeError("Each row of the matrix must have the same size")

    if type(div) not in [int, float]:
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")
    new_list = []
    for i in matrix:
        new_list.append(list(map(lambda x: round(x / div, 2), i)))
    return new_list

#!/usr/bin/python3
#

def square_matrix_simple(matrix=[]):
    new = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]
    for i in range(0, 3):
        for j in range(0, 3):
            new[i][j] = matrix[i][j] * matrix[i][j]
    return new

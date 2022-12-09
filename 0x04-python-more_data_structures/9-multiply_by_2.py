#!/usr/bin/python3
"""
function returns a new dictionary with all values multiplied by 2
"""


def multiply_by_2(a_dictionary):
    a = a_dictionary.copy()
    for i, j in a.items():
        a[i] = j * 2
    return a

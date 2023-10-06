#!/usr/bin/python3
"""A ALx module for TDD task 3"""


def print_square(size):
    """Prints a square of area size"""

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    i = 0
    while i < size:
        print(f"{'#' * size}")
        i += 1

#!/usr/bin/python3
"""class of square return the area"""


class Square:
    """square that give the area of square"""
    def __init__(self, size=0):

        self.Square__size = size
        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))

    def area(self):
        return self.Square__size ** 2

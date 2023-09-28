#!/usr/bin/python3
"""square class with exception"""


class Square:
    """square differentiate the argument weather an integer or not

    Attribute:
    size
    """
    def __init__(self, size=0):
        self.Square__size = size

        if not isinstance(size, int):
            raise (TypeError("size must be an integer"))
        if size < 0:
            raise (ValueError("size must be >= 0"))

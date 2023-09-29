#!/usr/bin/python3
"""add to number"""


def add_integer(a, b=98):
    """
    float arguments are typecasted to ints befor addition

    Return:
    a + b

    Args:
    a, b
    Raises:
        TypeError: if either of a or b is non-integer and non-float.
    """
    if ((not isinstance(a, int) and not isinstance(a, float))):
        raise TypeError("a must be an integer")
    if ((not isinstance(b, int) and not isinstance(b, float))):
        raise TypeError("b must be an integer")

    return (int(a) + int(b))

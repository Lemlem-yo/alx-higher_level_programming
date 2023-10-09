#!/usr/bin/python3
"""modify the BaseGeometry class"""


class BaseGeometry:
    """ add method of integer_validator"""
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        self.name = name
        self.value = value
        if not isinstance(value, int):
            raise TypeError("{name} must be an integer".format(name=name))
        if (value <= 0):
            raise ValueError("{name} must be greater than 0".format(name=name))

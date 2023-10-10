#!/usr/bin/python3
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Square class a chlid for Rectangle"""

    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        string = "[" + str(self.__class__.__bases__[0].__name__) + "] "
        string += str(self.__size) + "/" + str(self.__size)
        return string

#!/usr/bin/python3
"""calculate are and perimeter of the rectangle"""


class Rectangle:
    """Rectangle class"""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    
    @property
    def width(self):
        """width property"""
        return self.__width
    @width.setter
    def width(self, value):
        """width setter"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise TypeError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """height property"""
        return self.__height
    @height.setter
    def height(self, value):
        """height setter"""
        if not isinstance(value, int):
            raise TypeError("heigth must be an integer")
        if value < 0:
            raise TypeError("height must be >= 0")
        self.__height = value
         
    def area(self):
        """area of the rectangle"""
        return self.__height * self.__width
    def perimeter(self):
        """perimeter of the rectangle"""
        result = self.__height + self.__width
        return 2 * result 


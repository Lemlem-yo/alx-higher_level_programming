#!/usr/bin/python3
"""
    Rectangle module

    """


class Rectangle:
    """
        Rectangle Class

        Attribute:
            width (int): Private instance attr
            height (int) : Private instance attr
            number_of_instances (int) : Public Class attribute
            print_symbol (any type): Public Class attribute
        """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        """
            Init Rectangle Class

        Args:
            width (int): The width of rectangle
            height (int): Thhe height of rectangle
        """
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """
            width getter

            Return: The width of the Rectangle (int)
        """
        return self.__width

    @width.setter
    def width(self, value):
        """
            Width setter
        Args:
            Value (int) : a value to set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """
            height getter

        Return: the height of the rectangle (int)
        """
        return self.__height

    @height.setter
    def height(self, value):
        """
            height setter
        Args:
            value (int) : value to be set
        Raises:
            TypeError: When value is not int
            ValueError: When value is less than 0
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """
            Return Rectangle Area

        Return: (int) rectangle area
        """
        return self.__width * self.__height

    def perimeter(self):
        """
            Return the perimeter of rectangle

        Return : (int) rectangle perimeter
        """
        if self.__width == 0 or self.__height == 0:
            return 0
        return(self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """
            print the rectangle

        Return:
            printed rectangle widh '#'
            """
        if self.__width == 0 or self.__height == 0:
            return ""
        sy = str(self.print_symbol)
        return ((sy*self.__width + "\n")*self.__height)[:-1]

    def __repr__(self):
        """
        string representation of the rectangle

        Return:
            (str) representation of the rectangle
        """
        return 'Rectangle({}, {})'.format(self.__width, self.__height)

    def __del__(self):
        """
            Print message when instances deleted
        """
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """
            compare 2 rectangle
        Args:
            rect_1(Rectangle): First Rectangle
            rect_2(Rectangle): Second Rectangle
        Raises:
            TypeError: If rect_1 is not instance of Rectangle
            TypeError: If rect_2 is not instance of rectangle
        Return:
            Biggest Rectangle (Rectangle)
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")
        Area1 = rect_1.area()
        Area2 = rect_2.area()
        if Area1 >= Area2:
            return rect_1
        return rect_2

    @classmethod
    def square(cls, size=0):
        """
        Make a square from a rectangle
        Args:
            size (int): the size of the square
        Returns:
            (Rectangle): instance of rectangle
        """
        return cls(size, size)

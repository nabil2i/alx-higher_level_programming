#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Class Rectangle
        Attributes:
            __width (int): width of the rectangle
            __height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """getter of __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter of __width"""
        if type(value) is not int:
            raise TypeError("width must be an integer")
        else:
            if value < 0:
                raise ValueError("width must be >= 0")
            else:
                self.__width = value

    @property
    def height(self):
        """getter of __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter of __height"""
        if type(value) is not int:
            raise TypeError("height must be an integer")
        else:
            if value < 0:
                raise ValueError("height must be >= 0")
            else:
                self.__height = value

    def area(self):
        """Returns the rectangle area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return 2 * (self.__width + self.__height)

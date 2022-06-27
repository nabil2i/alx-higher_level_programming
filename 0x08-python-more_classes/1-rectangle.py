#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Class Rectangle
        Attributes:
            __width (int): width of the rectangle
            __height (int): height of the rectangle
    """
    def __init__(self, width=0, height=0):
        """Initialize a rectangle"""
        self.width = width
        self.height = height

    @property
    """getter of __width"""
    def width(self):
        return self.__width

    @width.setter
    """setter of __width"""
    def width(self, value):
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

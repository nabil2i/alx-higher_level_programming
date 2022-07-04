#!/usr/bin/python3
"""Class BaseGeometry"""

BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """Class BaseGeometry

    Attributes:
        __width (int): width of the rectangle
        __height (int): height  of the rectangle
        """

    def __init__(self, width, height):
        """Initializes an instance"""
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height

    def area(self):
        """Computes the area of the rectanglge"""
        return self.__width * self.__height

    def __str__(self):
        """Magic method to print the rectangle"""
        return ("[Rectangle] {:d}/{:d}".format(self.__width, self.__height))

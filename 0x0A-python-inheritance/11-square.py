#!/usr/bin/python3
"""Class BaseGeometry"""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class Square

    Attributes:
        __size (int): size of the square
        """

    def __init__(self, size):
        """Initializes an instance"""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Computes the area of the rectangle"""
        return self.__size ** 2

    def __str__(self):
        """Prints the square"""
        return ("[Square] {:d}/{:d}".format(self.__size, self.__size))

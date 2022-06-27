#!/usr/bin/python3
"""Defines a Rectangle class"""


class Rectangle:
    """Class Rectangle
        Attributes:
            __width (int): width of the rectangle
            __height (int): height of the rectangle
            number_of_instances (int): number of instances
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        """Initialize a rectangle

        Args:
            width (int): width of the rectangle
            height (int): height of the rectangle

        """
        self.width = width
        self.height = height
        number_of_instances += 1

    def __str__(self):
        """Prints the rectangle with the character #
        or returns an empty string
        """
        if self.__width == 0 or self.__height == 0:
            return ''
        rect = ''
        for i in range(self.__height):
            for j in range(self.__width):
                rect = rect + '#'
            rect = rect + '\n'
        return rect[:-1]

    def __repr__(self):
        """Returns a string representation of the rectangle
        to be able to recreate a new instance by using eval()"""
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """Deletes an instance of Rectangle"""
        number_of_instances -= 1
        print("Bye rectangle...")

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

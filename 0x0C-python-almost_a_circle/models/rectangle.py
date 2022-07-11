#!/usr/bin/python3
"""Module rectangle
Defines the class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle derived from Base
    """

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initializes an instance of Rectangle

        Args:
            __width (int): width of the rectangle
            __height (int): height of the rectangle
            __x (int): position on x axis
            __y (int): position of y axis
        """

        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

        @property
        def width(self):
            """Getter of __width"""
            return self.__width

        @property
        def height(self):
            """Getter of __height"""
            return self.__height

        @property
        def x(self):
            """Getter of __x"""
            return self.__x

        @property
        def y(self):
            """Getter of __y"""
            return self.__y

        @width.setter
        def width(self, width):
            """Setter of __width"""
            self.__width = width

        @height.setter
        def height(self, height):
            """Setter of __height"""
            self.__height = height

        @x.setter
        def x(self, x):
            """Setter of __x"""
            self.__x = x

        @y.setter
        def y(self, y):
            """Setter of __y"""
            self.__y = y

#!/usr/bin/python3
"""Module rectangle
Defines the class rectangle
"""
from models.base import Base


class Rectangle(Base):
    """class Rectangle derived from Base

    Public instance methods:
        - area()
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
    def width(self, value):
        """Setter of __width"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @height.setter
    def height(self, value):
        """Setter of __height"""

        if type(value) is not int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @x.setter
    def x(self, value):
        """Setter of __x"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @y.setter
    def y(self, value):
        """Setter of __y"""

        if type(value) is not int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area value of the Rectangle instance"""

        return self.__width * self.__height

    def display(self):
        """prints in stdout the Rectangle instance
        with the character #
        """
        for y in range(self.__y):
            print()
        for i in range(self.__height):
            for x in range(self.__x):
                print(" ", end="")
            for j in range(self.__width):
                print("#", end="")
            print()

    def __str__(self):
        """returns [Rectangle] (<id>) <x>/<y> - <width>/<height>"""

        return "[Rectangle] ({}) {}/{} - {}/{}".format(
                self.id, self.__x, self.__y, self.__width, self.__height)

    def update(self, *args, **kwargs):
        """assigns an argument to each attribute
        or a key/value argument to attributes"""

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.width = args[1]
            if len(args) > 2:
                self.height = args[2]
            if len(args) > 3:
                self.x = args[3]
            if len(args) > 4:
                self.y = args[4]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "width":
                    self.width = value
                if key == "height":
                    self.height = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

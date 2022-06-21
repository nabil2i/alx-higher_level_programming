#!/usr/bin/python3
"""Defines a class Suare"""


class Square:
    """Defines a square

    Attributes:
        __size (int): size of a side of the square
    """
    def __init__(self, size=0):
        """Initializes a square

        Args:
            size (int): size of a side of the square

            Returns: None
        """
        self.size = size

    @property
    def size(self):
        """getter of __size

        Returns:
            The size of the square
        """
        return self.__size

    @size.setter
    def size(self, value):
        """setter of __size

        Args:
            value (int): size of a side of the square

        Returns: None

        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        else:
            if size < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = size

    def area(self):
        """Returns the current square area

        Args:
            Returns: square area
        """
        return self.__size ** 2

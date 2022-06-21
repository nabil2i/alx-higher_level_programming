#!/usr/bin/python3
"""Defines a class Suare"""


class Square:
    """Defines a square

    Attributes:
        __size (int): size of a side of the square
        __position (tuple): position of the square
    """

    def __init__(self, size=0, position=(0, 0)):
        """Initializes a square

        Args:
            size (int): size of a side of the square
            position (tuple): coordinates

            Returns: None
        """
        self.size = size
        self.position = position

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

        Returns:
            None
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        else:
            if value < 0:
                raise ValueError("size must be >= 0")
            else:
                self.__size = value

    @property
    def position(self):
        """getter of __position

        Returns:
            Position of the square
        """
        return self.__position

    @position.setter
    def position(self, value):
        """setter of __position

        Args:
            value (typle): position of square

        Returns:
            None
        """
        if not isinstance(value, tuple) or len(value) != 2:
            raise TypeError("position must be a tuple of 2 positive integers")
        if not isinstance(value[0], int) or not isinstance(value[1], int):
            raise TypeError("position must be a tuple of 2 positive integers")
        if value[0] < 0 or value[1] < 0:
            raise TypeError("position must be a tuple of 2 positive integers")
        else:
            self.__position = value

    def area(self):
        """Returns the current square area

        Args:
            Returns: square area
        """
        return self.__size ** 2

    def my_print(self):
        """Prints in stdout the square
        at the given position

        Returns:
            None
        """
        if self.__size == 0:
            print()
            return
        for y in range(self.__position[1]):
            print()
        for i in range(self.__size):
            for x in range(self.__position[0]):
                print(" ", end="")
            for j in range(self.__size):
                print("#", end="")
            print()

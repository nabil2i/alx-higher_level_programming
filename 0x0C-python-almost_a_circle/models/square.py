#!usr/bin/python3
"""Module square
defines a a class square that derives from rectangle
"""

from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square derived from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise and instance of Square
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getterof size"""

        return self.__width

    @size.setter
    def size(self, value):
        """Setter for size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__height = value
        self.__width = value

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""

        return "return [Square] ({}) {}/{} - {}".format(
                self.id, self.__x, self.__y, self.__width)

#!/usr/bin/python3
"""Module square
defines a a class square that derives from rectangle
"""


from models.base import Base
from models.rectangle import Rectangle


class Square(Rectangle):
    """class Square derived from Rectangle
    """

    def __init__(self, size, x=0, y=0, id=None):
        """Initialise an instance of Square

        Args:
            __size: size of the square
            __x: position on x axis
            __y: position on y axix
            id: id of the instance of a square
        """

        self.size = size
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """Getter of size"""

        return self.__width

    @size.setter
    def size(self, value):
        """Setter for size"""

        if type(value) is not int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
        self.__height = value

    def __str__(self):
        """returns [Square] (<id>) <x>/<y> - <size>"""

        return "[Square] ({}) {}/{} - {}".format(
                self.id, self.x, self.y, self.__width)

    def update(self, *args, **kwargs):
        """assigns attributes

        Args:
            id :
            size :
            x :
            y :
        """

        if args is not None and len(args) != 0:
            if len(args) >= 1:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) > 2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            for key, value in kwargs.items():
                if key == "id":
                    self.id = value
                if key == "size":
                    self.size = value
                if key == "x":
                    self.x = value
                if key == "y":
                    self.y = value

#!/usr/bin/python3
"""Module base
Base class for of all other classes
"""

import json
import os
import csv


class Base:
    """class Base

    Attributes:
        __nb_objects (int): private class attribute
    """

    __nb_objects = 0

    def __init__(self, id=None):
        """Initialiazes an instance of Base

        Args:
            id (int): id of an instance of Base
        """

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """returns the JSON string representation
        of list_dictionaries
        """

        if list_dictionaries is None or list_dictionaries == []:
            return "[]"
        return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        writes the JSON string representation
        of list_objs to a file
        """

        if list_objs is None:
            my_str = "[]"
        else:
            my_str = cls.to_json_string([o.to_dictionary() for o in list_objs])
        filename = cls.__name__ + ".json"
        with open(filename, 'w') as f:
            f.write(my_str)

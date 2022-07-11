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

    @staticmethod
    def from_json_string(json_string):
        """returns the list of the JSON
        string representation json_string
        """

        my_list = []
        if json_string is not None and json_string != '':
            my_list = json.loads(json_string)
        return my_list

    @classmethod
    def create(cls, **dictionary):
        """returns an instance with all attributes already set
        """
        if cls.__name__ == 'Rectangle':
            dummy = cls(1, 1)
        if cls.__name__ == 'Square':
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """returns a list of instances"""

        filename = cls.__name__ + ".json"
        my_list = []
        if not os.path.exists(filename):
            return my_list
        with open(filename, 'r') as f:
            l = = f.read()
            my_dicts = cls.from_json_string(l)
            for dico in my_dicts:
                my_list.append(cls.create(**dico))
        return my_list

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """serializes in CSV"""

    @classmethod
    def load_from_file_csv(cls):
        """deserializes in CSV"""

    @staticmethod
    def draw(list_rectangles, list_squares):
        """opens a window and draws all the
        Rectangles and Squares
        """

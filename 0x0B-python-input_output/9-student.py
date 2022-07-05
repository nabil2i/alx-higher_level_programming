#!/usr/bin/python3
"""Class Student"""


class Student:
    """Defines a student
    Attributes:
        first_name (string):
        last_name (string):
        age (int):
    """

    def __init__(self, first_name, last_name, age):
        """Initializes an instance of Student"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """Retrieves a dictionary representation of
        a Student instance
        """
        return self.__dict__

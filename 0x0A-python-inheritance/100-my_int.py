#!/usr/bin/python3
"""Class MyInt"""


class MyInt(int):
    """class MyInt"""
    def __new__(cls, *args, **kwargs):
        """new instance oef the class"""
        return super(MyInt, cls).__new__(cls, *args, **kwargs)

    def __eq__(self, other):
        """!= becomes =="""
        return int(self) != other

    def __ne__(self, other):
        """== becomes !="""
        return int(self) == other

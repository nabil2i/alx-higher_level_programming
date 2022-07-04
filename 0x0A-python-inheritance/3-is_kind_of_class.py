#!/usr/bin/python3
"""Function is_kind_of_class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of, or an instance
    of a class that inherited from, the specified class
    """
    return isinstance(obj, a_class)

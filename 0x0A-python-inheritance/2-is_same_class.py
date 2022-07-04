#!/usr/bin/python3
"""Function is_same_class"""


def is_same_class(obj, a_class):
    """Returns True if the object is exactly an
    instance of the specified class. Otherwise False"""
    return type(obj) == a_class

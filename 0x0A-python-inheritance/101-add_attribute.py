#!/usr/bin/python3
"""Function add_attribute"""


def add_attribute(obj, attr, value):
    """Checks if an attribute can be added to an object

    Args:
        obj: object to add attribute to
        attr: the attribute to add
        value: value of the attribute attr
    """
    if not hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    if hasattr(obj, '__slots__') and not hasattr(obj, '__dict__'):
        raise TypeError("can't add new attribute")
    setattr(obj, attr, value)

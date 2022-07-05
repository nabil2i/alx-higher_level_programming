#!/usr/bin/python3
"""Function class_to_json"""


def class_to_json(obj):
    """Returns the dictionary description with simple data
    structure (list, dictionary, string, integer an dboolean)
    for JSON serializationof an object
    """
    return obj.__dict__

#!/usr/bin/python3
"""Function from_json_string"""
import json


def from_json_string(my_str):
    """returns an object (Python data structure)
    represented by a JSON string
    """
    return json.load(my_str)

#!/usr/bin/python3
"""Function save_to_json_file"""

import json


def save_to_json_file(my_str, filename):
    """Writes an Object to a text file using JSON
    representation
    """
    with open(filename, "w", encoding="utf-8") as f:
        json.dump(my_obj, f)

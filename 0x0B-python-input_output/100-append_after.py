#!/usr/bin/python3
"""Function append_after
"""


def append_after(filename="", search_string="", new_string=""):
    """Inserts a line of text to a file, after each line containing
    a specific string
    """
    with open(filename, "r", encoding="utf-8") as f:
        lines = f.readlines()

    with open(filename, "w", encoding="utf-8") as f2:
        my_str = ""
        for line in lines:
            my_str += line
            if search_string in line:
                my_str += new_string
        f2.write(my_str)

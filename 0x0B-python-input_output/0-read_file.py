#!/usr/bin/python3
"""Function read_file"""


def read_file(filename=""):
    """Reads a text file with utf8 encoding
    and prints it to stdout
    """
    with open(filename, encoding='utf-8') as f:
        print(f.read())

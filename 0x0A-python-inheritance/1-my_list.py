#!/usr/bin/python3
"""MyList class"""


class MyList(list):
    """MyList inherits from list"""
    def __init__(self):
        """Initializes the object"""
        super().__init__()

    def print_sorted(self):
        """prints the sorted list in ascending order"""
        print(sorted(self))

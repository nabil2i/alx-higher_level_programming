#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    """prints a dictionary by ordered keys"""
    sorted_keys = sorted(a_dictionary)
    for key in sorted_keys:
        print("{}: {}".format(key, a_dictionary.get(key)))

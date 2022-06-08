#!/usr/bin/python3
def search_replace(my_list, search, replace):
    """replaces all occurrences of an element
    by another in a new list"""
    new_list = []
    for index, item in enumerate(my_list):
        if item == search:
            new_list.append(replace)
        else:
            new_list.append(item)
    return new_list

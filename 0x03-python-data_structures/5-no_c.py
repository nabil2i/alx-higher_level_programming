#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        my_string2 = my_string.copy()
        i = 0
        while i < len(my_string2):
            if my_string2[i] == 'c' or my_string2[i] == 'C':
                my_string2 = my_string2[:i] + my_string2[i + 1:]
            i += 1
        return my_string2

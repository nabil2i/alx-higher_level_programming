#!/usr/bin/python3
def no_c(my_string):
    my_string2 = my_string.translate({ord(i): None for i in 'cC'})
    return my_string2

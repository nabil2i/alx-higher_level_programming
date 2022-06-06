#!/usr/bin/python3
def max_integer(my_list=[]):
    if my_list:
        i, maxInt = 0, my_list[0]
        while i < len(my_list):
            if (my_list[i] > maxInt):
                    maxInt = my_list[i]
            i += 1
        return maxInt
    else:
        return None

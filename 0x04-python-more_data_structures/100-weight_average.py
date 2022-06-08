#!/usr/bin/python3
def weight_average(my_list=[]):
    """returns the weighted average of all integers tuple"""
    if not my_list:
        return 0
    average, coef = 0, 0
    for t in my_list:
        average += t[0] * t[1]
        coef += t[1]
    return float(average / coef)

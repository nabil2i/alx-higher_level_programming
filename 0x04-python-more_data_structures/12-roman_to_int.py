#!/usr/bin/python3
def roman_to_int(roman_string):
    if type(roman_string) != str or roman_string == None:
        return 0
    table = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    roman_int = 0
    for idx in range(len(roman_string)):
        if idx > 0 and table[roman_string[idx]] > table[roman_string[idx - 1]]:
                roman_int += table[roman_string[idx]] -\
                                2 * table[roman_string[idx - 1]]
        else:
            roman_int += table[roman_string[idx]]
    return deci

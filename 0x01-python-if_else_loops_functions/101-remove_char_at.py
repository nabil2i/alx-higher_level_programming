#!/usr/bin/python3
def remove_char_at(str, n):
    str2 = ''
    i = 0
    for j in str:
        if i != n:
            str2 = str2 + str[i]
        i = i + 1
    return str2

#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_val = max(a_dictionary.keys(), key=(lambda new_k: a_dictionary[new_k]))
    return

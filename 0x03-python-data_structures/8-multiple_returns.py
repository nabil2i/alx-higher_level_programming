#!/usr/bin/python3
def multiple_returns(sentence):
    length = 0;
    first = None
    if sentence:
        length = len(sentence)
        first = sentence[0]
    tuple_sentence = (length, first)
    return tuple_sentence


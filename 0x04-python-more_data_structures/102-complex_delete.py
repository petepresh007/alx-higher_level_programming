#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    l = a_dictionary.copy()
    for k, v in l.items():
        if value == v:
            a_dictionary.pop(k)
    return a_dictionary


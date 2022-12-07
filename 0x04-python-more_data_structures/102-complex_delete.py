#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    for ky, vl in list(a_dictionary.items()):
        if value == vl:
            del a_dictionary[ky]
    return (a_dictionary)

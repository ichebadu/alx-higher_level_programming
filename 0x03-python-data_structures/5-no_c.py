#!/usr/bin/python3
def no_c(my_string):
    str_new = ""
    for x in my_string:
        if x != 'c' and x != 'C':
            str_new = str_new + x
    return str_new

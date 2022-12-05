#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    list_new = []
    for integer in my_list:
        if integer % 2 == 0:
            list_new.append(True)
        else:
            list_new.append(False)
    return list_new

#!/usr/bin/python3
def weight_average(my_list=[]):
    sc = 0
    wd = 0
    if my_list:
        for n in my_list:
            wd += n[0] * n[1]
            sc += + n[1]
        return wd / sc
    return 0

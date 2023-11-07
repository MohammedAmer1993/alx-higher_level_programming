#!/usr/bin/pythonn3
def max_integer(my_list=[]):
    if my_list:
        tmp = 0
        for i in my_list:
            if i > tmp:
                tmp = i
        return tmp
    else:
        return None

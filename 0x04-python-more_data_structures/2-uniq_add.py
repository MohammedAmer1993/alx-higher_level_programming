#!/usr/bin/python3
def uniq_add(my_list=[]):
    un = set(my_list)
    num = 0
    for i in un:
        num += i
    return num

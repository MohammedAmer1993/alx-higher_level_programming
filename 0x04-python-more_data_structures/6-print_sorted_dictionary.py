#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary):
    alist = list(a_dictionary.keys())
    alist.sort()
    for i in alist:
        print("{}: {}".format(i, a_dictionary.get(i)))

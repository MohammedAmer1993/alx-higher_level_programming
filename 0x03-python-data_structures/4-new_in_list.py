#!/usr/bin/python3
def new_in_list(my_list, idx, element):
    if my_list:
        if idx < 0 or idx >= len(my_list):
            return my_list.copy()
        else:
            list_cp = my_list.copy()
            list_cp[idx] = element
            return list_cp

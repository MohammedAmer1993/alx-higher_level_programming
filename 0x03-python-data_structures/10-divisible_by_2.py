#!/usr/bin/python3
def divisible_by_2(my_list=[]):
    if my_list:
        ll = []
        for i in my_list:
            if i % 2 == 0:
                ll.append(True)
            else:
                ll.append(False)
        return ll
    else:
        return None

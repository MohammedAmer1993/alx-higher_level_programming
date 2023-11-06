#!/usr/bin/python3
def no_c(my_string):
    if my_string:
        string = my_string.copy()
        for i in range(len(string)):
            if string[i] == 'c' or string[i] == 'C':
                string.pop(i)
        return string

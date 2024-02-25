#!/usr/bin/python3
"""Module for adding intgers all of tests are found in /tests"""


def add_integer(a, b=98):
    if type(a) != int or type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int or type(b) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))


if __name__ == "__main__":
    import doctest
    doctest.testfile("/tests/0-add_integer.txt")

#!/usr/bin/python3
"""Module for adding intgers all of tests are found in /tests
Test case for this module is in test dirctory
"""


def add_integer(a, b=98):
    """add two intger numbers
    Args:
        a (int): the frist argument
        b (int): the second number, defaults to 98
    Return: the sum of two numbers"""

    if a in None or type(a) is not int and type(a) is not float:
        raise TypeError("a must be an integer")
    if type(b) is not int and type(b) is not float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

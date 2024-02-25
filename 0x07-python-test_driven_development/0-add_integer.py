#!/usr/bin/python3
"""Module for adding intgers all of tests are found in /tests"""


def add_integer(a, b=98):
    """add two intger numbers
    Args:
        a (int): the frist argument
        b (int): the second number, defaults to 98
    Return:
        the sum of two numbers
    """
    if type(a) != int and type(a) != float:
        raise TypeError("a must be an integer")
    if type(b) != int and type(b) != float:
        raise TypeError("b must be an integer")
    return (int(a) + int(b))

#!/usr/bin/python3
"""Module for printing square all of tests are found in /tests"""


def print_square(size):
    """print square
    Args:
        size (int): the size of square
    """
    if type(size) is float or type(size) is not int:
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")
    for i in range(size):
        for z in range(size):
            print("#", end="")
        print()

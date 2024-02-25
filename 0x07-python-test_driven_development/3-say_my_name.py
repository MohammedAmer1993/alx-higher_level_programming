#!/usr/bin/python3
"""Module for repeating a name all of tests are found in /tests"""


def say_my_name(first_name, last_name=""):
    """ say_my_name function
    Args:
        first_name (str): the frist name
        last_name (str): the last name defaults to empty string
    """
    if type(first_name) is not str:
        raise TypeError("first_name must be a string")
    elif type(last_name) is not str:
        raise TypeError("last_name must be a string")

    print("My name is {} {}".format(first_name, last_name), end="")

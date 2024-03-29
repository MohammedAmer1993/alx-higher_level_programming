#!/usr/bin/python3
"""Defines a class-checking function."""


def is_same_class(obj, a_class):
    """Check if an object is an instance of a class.

    Args:
        obj (any): The object to check.
        a_class (type): The class to compare obj to.
    Returns:
        If obj is instance of a_class - True.
        Otherwise - False.
    """
    if type(obj) == a_class:
        return True
    return False

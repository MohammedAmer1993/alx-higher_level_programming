#!/usr/bin/python3
"""Module for base class for other shapes to inherit from"""


class Base:
    """the base class of inheratance"""

    __nb_objects = 0

    def __init__(self, id=None):
        """constructor of base class

        Args:
            id (int): this is the uniqie id of each obj
        """
        if id is None:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
        else:
            self.id = id

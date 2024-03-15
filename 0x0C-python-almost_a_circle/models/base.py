#!/usr/bin/python3
"""Module for base class for other shapes to inherit from"""

import json


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

    @staticmethod
    def to_json_string(list_dictionaries):
        """static method that returns the JSON str of list of dictionaries

        Args:
            list_dictionaries (list[dict]): the list to be transformed
        """
        if not list_dictionaries:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    # @classmethod
    # def save_to_file(cls, list_objs):
    #     if list_objs is None:
    #         mylist = []
    #     else:
    #         mylist = list_objs
    #     name = cls.__name__ + ".json"
    #     with open(name, "w") as file:
    #         json.dump(file, mylist)

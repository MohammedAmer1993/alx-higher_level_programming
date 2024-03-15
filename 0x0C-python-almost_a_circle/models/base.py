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

    @classmethod
    def save_to_file(cls, list_objs):
        filename = cls.__name__ + ".json"

        if list_objs is None:
            with open(filename, "w") as file:
                file.write("")

        else:
            mylist = []
            for i in list_objs:
                mylist.append(i.to_dictionary())
            msg = cls.to_json_string(mylist)
            with open(filename, "w") as file:
                file.write(msg)

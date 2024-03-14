#!/usr/bin/python3
"""Module for Square class"""


from models.rectangle import Rectangle


class Square(Rectangle):
    """Square class"""

    def __init__(self, size, x=0, y=0, id=None):
        """Constructor of Square
        Args:
            size (int): the edge of square
            x (int): the X of square
            y (int): the Y of square
            id (int): the id of square
        """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value

    def __str__(self):
        """the string representation in the class"""
        msg = f"[Square] ({self.id}) {self.x}/{self.y} -"
        msg = msg + f" {self.width}"
        return msg

    def update(self, *args, **kwargs):
        """update method
        Args:
            args: tuple of positional arguments
            kwargs: dictionary of keyword arguments
        """
        args = list(args)
        if len(args) >= 2:
            args.insert(2, args[1])
        if "size" in kwargs.keys():
            tmp = kwargs["size"]
            kwargs.pop('size')
            kwargs["width"] = tmp
            kwargs["height"] = tmp
        if args:
            super().update(*args)
        else:
            super().update(**kwargs)

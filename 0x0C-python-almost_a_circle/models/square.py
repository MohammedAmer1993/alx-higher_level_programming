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

    def __str__(self):
        msg = f"[Square] ({self.id}) {self.x}/{self.y} -"
        msg = msg + f" {self.width}"
        return msg

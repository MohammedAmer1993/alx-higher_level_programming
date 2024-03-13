#!/usr/bin/python3
"""Module for class rectangle that inherts from base class"""

from .base import Base


class Rectangle(Base):
    """Rectangle class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Constructor of rectangle class

        Args:
            width (int): the width of rectangle
            height (int): the height of rectangle
            x (int): the """
        if type(width) is not int:
            raise TypeError("width must be an integer")
        if type(height) is not int:
            raise TypeError("height must be an integer")
        if width < 0:
            raise ValueError("width must be > 0")
        if height < 0:
            raise ValueError("height must be > 0")
        if type(x) is not int:
            raise TypeError("x must be an integer")
        if type(y) is not int:
            raise TypeError("y must be an integer")
        if x < 0:
            raise ValueError("x must be >= 0")
        if y < 0:
            raise ValueError("y must be >= 0")
        else:
            super().__init__(id)
            self.__x = x
            self.__y = y
            self.__width = width
            self.__height = height

    @property
    def width(self):
        """ getter for __width"""
        return self.__width

    @width.setter
    def width(self, value):
        """setter for __width
        Args:
            value (int): the new valu
        """
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        """ getter for __height"""
        return self.__height

    @height.setter
    def height(self, value):
        """setter for __heith
        Args:
            value (int): the new valu
        """
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        """ getter for __x"""
        return self.__x

    @x.setter
    def x(self, value):
        """setter for __x
        Args:
            value (int): the new valu
        """
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        """ getter for __y"""
        return self.__y

    @y.setter
    def y(self, value):
        """setter for __y
        Args:
            value (int): the new valu
        """
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

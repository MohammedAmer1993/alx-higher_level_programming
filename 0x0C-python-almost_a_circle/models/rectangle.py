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
        self.__y = value

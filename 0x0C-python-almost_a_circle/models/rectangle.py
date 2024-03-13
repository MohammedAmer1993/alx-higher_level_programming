#!/usr/bin/python3
"""Module for class rectangle that inherts from base class"""

from models.base import Base


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
        if width <= 0:
            raise ValueError("width must be > 0")
        if height <= 0:
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
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is not int:
            raise TypeError("width must be an integer")
        elif value <= 0:
            raise ValueError("width must be > 0")
        else:
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is not int:
            raise TypeError("height must be an integer")
        elif value <= 0:
            raise ValueError("height must be > 0")
        else:
            self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) is not int:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        else:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) is not int:
            raise TypeError("y must be an integer")
        elif value < 0:
            raise ValueError("y must be >= 0")
        else:
            self.__y = value

    def area(self):
        """Area method to return the area of Rect"""
        return self.__width * self.__height

    def display(self):
        """Display function to draw a rect using #

        Return:
            the shape of Rect
        """
        con = ""
        con2 = ""
        for i in range(self.__y):
            con2 += "\n"
        for i in range(self.__x):
            con += " "
        dis = ""
        for i in range(self.__height):
            dis += con
            for z in range(self.__width):
                dis += "#"
            dis += "\n"
        dis = con2 + dis
        print(dis, end="")
        return dis

    def __str__(self):
        """the string representation of Rect class

        Return:
            information of the class as string
        """
        msg = f"[Rectangle] ({self.id}) {self.__x}/{self.__y} -"
        msg = msg + f" {self.__width}/{self.__height}"
        return msg

#!/usr/bin/python3

import unittest
from models.square import Square
from tests.test_models.test_rectangle import test_rect


class test_square(test_rect):

    testobj = Square(10, 1, 1, 98)

    def test_getter_width(self):
        self.assertEqual(self.testobj.width, 10)

    def test_getter_height(self):
        self.assertEqual(self.testobj.height, 10)

    def test_getter_x(self):
        self.assertEqual(self.testobj.x, 1)

    def test_getter_y(self):
        self.assertEqual(self.testobj.y, 1)

    def test_str(self):
        test = Square(5, 0, 0, 98)
        msg = "[Square] (98) 0/0 - 5"
        self.assertEqual(test.__str__(), msg)

    def test_size_getter(self):
        test_square.testobj.size = 30
        self.assertEqual(test_square.testobj.size, 30)


if __name__ == "__main__":
    unittest.main()

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

    def test_size_value(self):
        with self.assertRaises(ValueError):
            test_square.testobj.size = -3

    def test_size_type(self):
        with self.assertRaises(TypeError):
            test_square.testobj.size = "hi"

    def test_update_square(self):
        test_square.testobj.update(1, 2, 3, 4)
        msg = "[Square] (1) 3/4 - 2"
        self.assertEqual(test_square.testobj.__str__(), msg)

    def test_update2_Square(self):
        test_square.testobj.update(id=89, x=2, y=2, size=32)
        msg = "[Square] (89) 2/2 - 32"
        self.assertEqual(test_square.testobj.__str__(), msg)

    def test_dict_square(self):
        test = Square(10, 2, 1, 100)
        dict1 = test.to_dictionary()
        dict2 = {'id': 100, 'x': 2, 'size': 10, 'y': 1}
        self.assertEqual(dict1, dict2)


if __name__ == "__main__":
    unittest.main()

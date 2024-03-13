#!/usr/bin/python3
"""Module to test rectangle class"""
import unittest
from models.rectangle import Rectangle


class test_rect(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.testobj = Rectangle(20, 10, 0, 0)

    @classmethod
    def tearDownClass(cls):
        del cls.testobj

    def test_getter_width(self):
        self.assertEqual(self.testobj.width, 20)

    def test_getter_height(self):
        self.assertEqual(self.testobj.height, 10)

    def test_getter_x(self):
        self.assertEqual(self.testobj.x, 0)

    def test_getter_y(self):
        self.assertEqual(self.testobj.y, 0)

    def test_setter_width(self):
        test_rect.testobj.width = 30
        res = test_rect.testobj.width
        self.assertEqual(res, 30)

    def test_setter_height(self):
        test_rect.testobj.height = 40
        res = test_rect.testobj.height
        self.assertEqual(res, 40)

    def test_setter_x(self):
        test_rect.testobj.x = 5
        res = test_rect.testobj.x
        self.assertEqual(res, 5)

    def test_setter_y(self):
        test_rect.testobj.y = 6
        res = test_rect.testobj.y
        self.assertEqual(res, 6)

    def test_width_type(self):
        with self.assertRaises(TypeError):
            test_rect.testobj.width = "hi"

    def test_width_type_inst(self):
        with self.assertRaises(TypeError):
            test = Rectangle("str", 5, 5, 5)

    def test_width_value(self):
        with self.assertRaises(ValueError):
            test_rect.testobj.width = -6

    def test_width_value_inst(self):
        with self.assertRaises(ValueError):
            test = Rectangle(-5, 5)

    def test_height_type(self):
        with self.assertRaises(TypeError):
            test_rect.testobj.height = "hi"

    def test_height_type_inst(self):
        with self.assertRaises(TypeError):
            test = Rectangle(5, "str", 5, 5)

    def test_height_value(self):
        with self.assertRaises(ValueError):
            test_rect.testobj.height = -6

    def test_height_value_inst(self):
        with self.assertRaises(ValueError):
            test = Rectangle(5, -5)

    def test_x_type(self):
        with self.assertRaises(TypeError):
            test_rect.testobj.x = "hi"

    def test_x_type_inst(self):
        with self.assertRaises(TypeError):
            test = Rectangle(5, 5, "str", 5)

    def test_x_value(self):
        with self.assertRaises(ValueError):
            test_rect.testobj.x = -3

    def test_x_value_inst(self):
        with self.assertRaises(ValueError):
            test = Rectangle(5, 5, -5, 5)

    def test_y_type(self):
        with self.assertRaises(TypeError):
            test_rect.testobj.y = "hi"

    def test_y_type_inst(self):
        with self.assertRaises(TypeError):
            test = Rectangle(5, 5, 5, "str")

    def test_y_value(self):
        with self.assertRaises(ValueError):
            test_rect.testobj.y = -3

    def test_x_value_inst(self):
        with self.assertRaises(ValueError):
            test = Rectangle(5, 5, 5, -5)

    def test_area(self):
        test = Rectangle(4, 3)
        self.assertEqual(test.area(), 12)

    def test_display(self):
        test = Rectangle(2, 3)
        self.assertEqual(test.display(), "##\n##\n##\n")

    def test_str(self):
        test = Rectangle(3, 4, 1, 2, 98)
        msg = "[Rectangle] (98) 1/2 - 3/4"

        self.assertEqual(test.__str__(), msg)


if __name__ == "__main__":
    unittest.main()

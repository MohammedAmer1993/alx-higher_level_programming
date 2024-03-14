#!/usr/bin/python3
"""Module to test rectangle class"""
import unittest
from models.rectangle import Rectangle


class test_rect(unittest.TestCase):

    testobj = Rectangle(20, 10, 0, 0)

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

    def test_str(self):
        test = Rectangle(3, 4, 1, 2, 98)
        msg = "[Rectangle] (98) 1/2 - 3/4"

        self.assertEqual(test.__str__(), msg)

    def test_display(self):
        test = Rectangle(3, 2, 1, 3)
        msg = "\n\n\n ###\n ###\n"
        self.assertEqual(test.display(), msg)

    def test_update(self):
        test_rect.testobj.update(89, 2, 3, 4, 5)
        msg = "[Rectangle] (89) 4/5 - 2/3"
        self.assertEqual(test_rect.testobj.__str__(), msg)

    def test_update2(self):
        test_rect.testobj.update(89, x=2, y=3, height=4, width=5)
        msg = "[Rectangle] (89) 2/3 - 5/4"
        self.assertEqual(test_rect.testobj.__str__(), msg)

    def test_dict(self):
        test = Rectangle(10, 2, 1, 9, 100)
        dict1 = test.to_dictionary()
        dict2 = {'x': 1, 'y': 9, 'id': 100, 'height': 2, 'width': 10}
        self.assertEqual(dict1, dict2)


if __name__ == "__main__":
    unittest.main()

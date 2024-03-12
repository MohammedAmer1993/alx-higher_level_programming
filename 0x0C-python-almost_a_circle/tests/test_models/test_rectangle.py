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


if __name__ == "__main__":
    unittest.main()

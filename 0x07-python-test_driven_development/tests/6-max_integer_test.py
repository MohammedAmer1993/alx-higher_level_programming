#!/usr/bin/python3
import unittest

max_integer = __import__("6-max_integer").max_integer


class testmaxint(unittest.TestCase):

    def test_none(self):
        self.assertIsNone(max_integer([]))

    def test_type(self):
        self.assertRaises(TypeError, max_integer, 7)

    def test_num(self):
        self.assertEqual(max_integer([2, 8, 7, 6, 3]), 8)

    def test_num2(self):
        self.assertEqual(max_integer([2, -8, 7, -6, 3]), 7)

    def test_num3(self):
        self.assertEqual(max_integer([2.32, -8, 5.14, -66, 3]), 5.14)

    def test_num4(self):
        self.assertEqual(max_integer([32, 8, 7, 6, 3]), 32)

    def test_num5(self):
        self.assertEqual(max_integer([2, 8, 7, 6, 67]), 67)

    def test_num6(self):
        self.assertEqual(max_integer([67]), 67)

    def test_elem(self):
        self.assertRaises(TypeError, max_integer, [2, "vo", True, [3]])


if __name__ == "__main__":
    unittest.main()

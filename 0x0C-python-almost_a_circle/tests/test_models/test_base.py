#!/usr/bin/python3
"""test module for base class"""

import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def test_id(self):
        testobj = Base(32)
        self.assertEqual(testobj.id, 32)

    def test_to_json1(self):
        self.assertEqual(Base.to_json_string([]), "[]")

    def test_to_json2(self):
        self.assertEqual(Base.to_json_string(None), "[]")

    def test_to_json3(self):
        dict1 = {"name": "Mohammed", "age": 31}
        mylist = []
        mylist.append(dict1)
        msg = r'[{"name": "Mohammed", "age": 31}]'
        self.assertEqual(Base.to_json_string(mylist), msg)


if __name__ == "__main__":
    unittest.main()

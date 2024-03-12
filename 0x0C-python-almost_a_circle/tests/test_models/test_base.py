#!/usr/bin/python3
"""test module for base class"""

import unittest
from models.base import Base


class test_base(unittest.TestCase):

    def test_id(self):
        testobj = Base(32)
        self.assertEqual(testobj.id, 32)


if __name__ == "__main__":
    unittest.main()

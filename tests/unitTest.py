import unittest
import time
import sys

from astar.pathFinder import PathFinder

class TestPathFinder(unittest.TestCase):
    def setUp(self):
        print("-----------test start-----------")

    def test_case01(self):
        print("test case 01")

    def test_case02(self):
        print("test case 02")

    @unittest.skipIf(True, "test this keyword")
    def test_case03(self):
        print("test case 03")
        self.assertEqual(1, 1)
        self.assertEqual(2, 2)

    def tearDown(self):
        print("-----------test end-----------")

# python -m unittest tests.unitTest.TestPathFinder.test_case01
# python -m unittest tests.unitTest.TestPathFinder
if __name__ == '__main__':
    unittest.main()
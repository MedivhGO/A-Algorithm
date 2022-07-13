import unittest
import time
import sys

from astar.pathFinder import PathFinder, Point


class TestPathFinder(unittest.TestCase):
    def setUp(self):
        pass

    def test_case01(self):
        print("test case 01")

    def test_case02(self):
        print("test case 02")

    # @unittest.skipIf(True, "test this keyword")
    def test_case03(self):
        print("test case 03")
        self.assertEqual(1, 1)
        self.assertEqual(2, 2)

    def test_case04(self):
        path_finder = PathFinder()
        print(path_finder.diff_x, path_finder.diff_z)
        print(path_finder.check_map(0, 2))
        # for line in path_finder.game_map:
        #     print line

        start_point = Point(-5, 14)
        end_point = Point(-5, 7)

        path = path_finder.find_path(start_point, end_point)

        for p in path:
            print(p.X, p.Z)

    def tearDown(self):
        pass


# python -m unittest tests.unitTest.TestPathFinder.test_case01
# python -m unittest tests.unitTest.TestPathFinder
if __name__ == '__main__':
    unittest.main()

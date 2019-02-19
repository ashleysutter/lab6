import unittest
from sorts import *

class TestLab4(unittest.TestCase):

    def test_simple(self):
        nums = [23, 10]
        comps = selection_sort(nums)
        self.assertEqual(comps, 1)
        self.assertEqual(nums, [10, 23])

    def test_selection(self):
        nums = [3, 7, 2, 11]
        comps = selection_sort(nums)
        self.assertEqual(comps, 6)
        self.assertEqual(nums, [2, 3, 7, 11])

    def test_insertion(self):
        nums = [3, 7, 2, 11]
        comps = insertion_sort(nums)
        #self.assertEqual(comps, 6)
        self.assertEqual(nums, [2, 3, 7, 11])

    def test_insertion_1(self):
        nums = [0, 15, 5, 1, 0, 20, 25, 30, 35, 40]
        comps = insertion_sort(nums)
        self.assertEqual(comps, 15)
        self.assertEqual(nums, [0, 0, 1, 5, 15, 20, 25, 30, 35, 40])


if __name__ == '__main__': 
    unittest.main()

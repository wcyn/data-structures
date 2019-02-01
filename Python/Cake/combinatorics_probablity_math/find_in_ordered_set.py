# https://www.interviewcake.com/question/python/find-in-ordered-set?course=fc1&section=combinatorics-probability-math
# Suppose we had a list ↴ of nn integers sorted in ascending order.
# How quickly could we check if a given integer is in the list?
import unittest


def binary_search(num_list, target):
    floor, ceil = 0, len(num_list) - 1
    while floor <= ceil:
        mid = floor + ((ceil - floor) // 2)
        if num_list[mid] == target:
            return True
        elif num_list[mid] > target:
            ceil = mid - 1
        else:
            floor = mid + 1
    return False


nums = [1, 45, 50, 67, 68, 69, 91, 102]
print(binary_search(nums, 68))
print(binary_search(nums, 70))


class Test(unittest.TestCase):

    def test_empty_list(self):
        result = binary_search([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = binary_search([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = binary_search([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = binary_search([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = binary_search([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)

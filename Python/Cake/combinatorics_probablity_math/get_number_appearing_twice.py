# https://www.interviewcake.com/question/python/which-appears-twice?course=fc1&section=combinatorics-probability-math
# I have a list of n + 1n+1 numbers. Every number in the range 1..n1..n
# appears once except for one number that appears twice.
#
# Write a function for finding the number that appears twice.
import unittest


def get_duplicate_number(nums):
    n = len(nums) - 1
    triangular_series_sum = (n + 1) * (n/2)
    nums_sum = 0
    for num in nums:
        nums_sum += num
    return int(nums_sum - triangular_series_sum)


num_list = [1, 3, 2, 4, 3]
print(get_duplicate_number(num_list))


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = get_duplicate_number([1, 2, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = get_duplicate_number([4, 1, 3, 4, 2])
        expected = 4
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = get_duplicate_number([1, 5, 9, 7, 2, 6, 3, 8, 2, 4])
        expected = 2
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

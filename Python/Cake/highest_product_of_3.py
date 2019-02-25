# https://www.interviewcake.com/question/python/highest-product-of-3?course=fc1&section=greedy
# Given a list of integers, find the highest product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.
import unittest


def get_highest_product_of_three_incorrect_for_all_negative_numbers_list(int_list):

    highest_product_of_2 = int_list[0] * int_list[1]
    lowest_product_of_2 = int_list[0] * int_list[1]
    highest = max(int_list[0], int_list[1])
    lowest = min(int_list[0], int_list[1])
    highest_product_of_3 = int_list[0] * int_list[1] + int_list[2]

    for index in range(2, len(int_list)):
        current = int_list[index]

        highest_product_of_3 = max(
            highest_product_of_3,
            current * highest_product_of_2,
            current * lowest_product_of_2
        )

        highest_product_of_2 = max(
            highest_product_of_2,
            current * highest,
            current * lowest
        )

        lowest_product_of_2 = min(
            lowest_product_of_2,
            current * highest,
            current * lowest
        )

        highest = max(highest, current)
        lowest = min(lowest, current)

    return highest_product_of_3


def get_highest_product_of_k_contiguous_elements(int_list, k):
    max_product = 1
    for index in range(0, k):
        max_product *= int_list[index]
    # print(max_product)

    previous_product = max_product
    for index in range(1, len(int_list) - k + 1):
        current_product = (previous_product // int_list[index-1]) * int_list[index+(k-1)]
        # print(current_product)
        max_product = max(max_product, current_product)
        previous_product = current_product

    return max_product


def get_highest_product_of_3(list_of_ints):
    if len(list_of_ints) < 3:
        raise ValueError('Less than 3 items!')

        # We're going to start at the 3rd item (at index 2)
        # so pre-populate highests and lowests based on the first 2 items.
        # We could also start these as None and check below if they're set
        # but this is arguably cleaner
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest = min(list_of_ints[0], list_of_ints[1])
    highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest_product_of_2 = list_of_ints[0] * list_of_ints[1]

    # Except this one--we pre-populate it for the first *3* items.
    # This means in our first pass it'll check against itself, which is fine.
    highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

    # Walk through items, starting at index 2
    for i in range(2, len(list_of_ints)):
        current = list_of_ints[i]

        # Do we have a new highest product of 3?
        # It's either the current highest,
        # or the current times the highest product of two
        # or the current times the lowest product of two
        highest_product_of_3 = max(highest_product_of_3,
                                   current * highest_product_of_2,
                                   current * lowest_product_of_2)

        # Do we have a new highest product of two?
        highest_product_of_2 = max(highest_product_of_2,
                                   current * highest,
                                   current * lowest)

        # Do we have a new lowest product of two?
        lowest_product_of_2 = min(lowest_product_of_2,
                                  current * highest,
                                  current * lowest)

        # Do we have a new highest?
        highest = max(highest, current)

        # Do we have a new lowest?
        lowest = min(lowest, current)

    return highest_product_of_3


nums = [1, 10, -5, 1, -100]
nums2 = [2, 5, 10, 1, 8, 9]
print(get_highest_product_of_3(nums2))
print(get_highest_product_of_k_contiguous_elements(nums2, 3))


class Test(unittest.TestCase):

    def test_short_list(self):
        actual = get_highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = get_highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = get_highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = get_highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            get_highest_product_of_3([1, 1])


unittest.main(verbosity=2)


# Extra exercise to get lowest sum of three
def three_sum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    if len(nums) < 3:
        return []

    smallest_2_sum_nums = tuple(nums[:2])
    smallest_2_sum = sum(smallest_2_sum_nums)
    smallest_3_sum_nums = tuple(nums[:3])
    smallest_3_sum = sum(smallest_3_sum_nums)
    min_num = min(smallest_3_sum_nums)

    for index in range(2, len(nums)):
        current_2_sum = min_num + nums[index]
        current_3_sum = smallest_2_sum + nums[index]
        if smallest_3_sum > current_3_sum:
            smallest_3_sum = current_3_sum
            smallest_3_sum_nums = smallest_2_sum_nums + (nums[index],)

        if smallest_2_sum > current_2_sum:
            smallest_2_sum = current_2_sum
            smallest_2_sum_nums = (min_num, nums[index])
        min_num = min(min_num, nums[index])
    return smallest_3_sum_nums

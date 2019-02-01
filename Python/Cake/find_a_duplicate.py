# Find a duplicate, Space Edition™.
# We have a list of integers, where:
#
# The integers are in the range 1..n1..n
# The list has a length of n+1n+1
# It follows that our list has at least one integer which appears at least twice.
# But it may have several duplicates, and each duplicate may appear more than twice.
#
# Write a function which finds an integer that appears more than once in our list.
# (If there are multiple duplicates, you only need to find one of them.)
#
# We're going to run this function on our new, super-hip MacBook Pro With Retina Display™.
# Thing is, the damn thing came with the RAM soldered right to the motherboard,
# so we can't upgrade our RAM. So we need to optimize for space!
import unittest


def find_a_duplicate(num_list):
    current_index = 0
    iters = 0
    while current_index < len(num_list):
        iters += 1
        current_num = num_list[current_index]
        if current_num == current_index + 1:
            current_index += 1
        else:
            # We need to swap this num to the right place
            # First check if it already exists at that index
            if current_num == num_list[current_num-1]:
                return current_num
            else:
                # Swap em
                num_list[current_index], num_list[current_num-1] = num_list[current_num-1], num_list[current_index]
    print('Iters: ', iters)
    return None


def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            if lower_range_floor <= item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
                lower_range_ceiling
                - lower_range_floor
                + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


def find_duplicate_non_destructive(num_list):
    if len(num_list) < 2:
        return None

    floor, ceil = 0, len(num_list)-2

    while floor < ceil:
        original_mid = floor + ((ceil - floor)//2)
        lower_range_floor, lower_range_ceil = floor, original_mid
        print(lower_range_floor, lower_range_ceil)
        higher_range_floor, higher_range_ceil = original_mid+1, ceil

        nums_in_lower_range = 0
        for num in num_list:
            if lower_range_floor + 1 <= num <= lower_range_ceil + 1:
                nums_in_lower_range += 1

        if nums_in_lower_range > original_mid + 1:
            # Duplicate is in the lower range
            floor, ceil = lower_range_floor, lower_range_ceil
            # print(floor, ceil)
        else:
            floor, ceiling = higher_range_floor, higher_range_ceil

    return floor + 1


nums = [6, 3, 1, 2, 4, 5]
n = [3, 5, 4, 2, 4, 6, 1]
n2 = [1, 2, 5, 3, 4, 5]
n3 = [1, 3, 2, 3]
# print(find_a_duplicate(n2))
# print(nums)
print(find_duplicate_non_destructive(n2))
# print(find_repeat(nums))

# Tests


class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)

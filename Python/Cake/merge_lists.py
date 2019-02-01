# https://www.interviewcake.com/question/python/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation
# Write a function to merge our lists of orders into one sorted list.

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


def merge_lists_repetitive(list1, list2):
    merged_list = []
    list1_ptr = list2_ptr = 0
    while list1_ptr < len(list1) and list2_ptr < len(list2):
        if list1[list1_ptr] < list2[list2_ptr]:
            merged_list.append(list1[list1_ptr])
            list1_ptr += 1
        elif list1[list1_ptr] > list2[list2_ptr]:
            merged_list.append(list2[list2_ptr])
            list2_ptr += 1
        else:
            merged_list.append(list1[list1_ptr])
            list1_ptr += 1
            list2_ptr += 1

    while list1_ptr < len(list1):
        merged_list.append(list1[list1_ptr])
        list1_ptr += 1
    while list2_ptr < len(list2):
        merged_list.append(list2[list2_ptr])
        list2_ptr += 1

    return merged_list


def merge_lists(my_list, alices_list):
    merged_list_size = len(my_list) + len(alices_list)
    my_list_index = alices_list_index = merged_list_index = 0
    merged_list = []

    while merged_list_index < merged_list_size:
        my_list_exhausted = my_list_index >= len(my_list)
        alices_list_exhausted = alices_list_index >= len(alices_list)
        if not my_list_exhausted and (
            alices_list_exhausted or my_list[my_list_index] < alices_list[alices_list_index]):
            merged_list.append(my_list[my_list_index])
            my_list_index += 1
        else:
            merged_list.append(alices_list[alices_list_index])
            alices_list_index += 1
        merged_list_index += 1

    return merged_list

print(merge_lists(my_list, alices_list))

import unittest
class Test(unittest.TestCase):

    def test_both_lists_are_empty(self):
        actual = merge_lists([], [])
        expected = []
        self.assertEqual(actual, expected)

    def test_first_list_is_empty(self):
        actual = merge_lists([], [1, 2, 3])
        expected = [1, 2, 3]
        self.assertEqual(actual, expected)

    def test_second_list_is_empty(self):
        actual = merge_lists([5, 6, 7], [])
        expected = [5, 6, 7]
        self.assertEqual(actual, expected)

    def test_both_lists_have_some_numbers(self):
        actual = merge_lists([2, 4, 6], [1, 3, 7])
        expected = [1, 2, 3, 4, 6, 7]
        self.assertEqual(actual, expected)

    def test_lists_are_different_lengths(self):
        actual = merge_lists([2, 4, 6, 8], [1, 7])
        expected = [1, 2, 4, 6, 7, 8]
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)
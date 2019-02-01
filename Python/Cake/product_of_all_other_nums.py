# https://www.interviewcake.com/question/python/product-of-other-numbers?course=fc1&section=greedy
# Write a function get_products_of_all_ints_except_at_index() that takes a list of
# integers and returns a list of the products.
import unittest

def get_product_of_all_other_nums(num_list):
    full_product = 1
    zero_count = 0
    for num in num_list:
        if num == 0:
            zero_count += 1
        full_product *= num if num else 1

    if zero_count > 1:
        return [0 for num in num_list]
    elif zero_count == 1:
        return [0 if num else full_product for num in num_list]

    return [full_product // num for num in num_list]


def get_product_of_all_other_nums_no_div(num_list):
    if len(num_list) < 2:
        raise IndexError("Getting products of all other numbers requires at least two numbers")
    products_before = [1]
    for index in range(len(num_list)-1):
        products_before.append(products_before[-1] * num_list[index])

    # print(products_before)
    # results = [None] * len(num_list)
    product_after = 1
    for index in range(len(num_list)):
        print(product_after)
        products_before[~index] *= product_after
        product_after *= num_list[~index]

    return products_before


nums = [1, 7, 0, 3, 0, 4]
print(get_product_of_all_other_nums(nums))
print(get_product_of_all_other_nums_no_div(nums))

# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)
# https://www.interviewcake.com/question/python/highest-product-of-3?course=fc1&section=greedy
# Given a list of integers, find the highest product you can get from three of the integers.
# The input list_of_ints will always have at least three integers.


def get_highest_product_of_three(int_list):

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


nums = [1, 10, -5, 1, -100]
nums2 = [2, 5, 10, 1, 8, 9]
print(get_highest_product_of_three(nums2))
print(get_highest_product_of_k_contiguous_elements(nums2, 3))


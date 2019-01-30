# https://www.interviewcake.com/question/python/which-appears-twice?course=fc1&section=combinatorics-probability-math
# I have a list of n + 1n+1 numbers. Every number in the range 1..n1..n
# appears once except for one number that appears twice.
#
# Write a function for finding the number that appears twice.


def get_duplicate_number(nums):
    n = len(nums) - 1
    triangular_series_sum = (n + 1) * (n/2)
    nums_sum = 0
    for num in nums:
        nums_sum += num
    return int(nums_sum - triangular_series_sum)


num_list = [1, 3, 2, 4, 3]
print(get_duplicate_number(num_list))

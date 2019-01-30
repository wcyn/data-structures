# https://www.interviewcake.com/question/python/find-in-ordered-set?course=fc1&section=combinatorics-probability-math
# Suppose we had a list ↴ of nn integers sorted in ascending order.
# How quickly could we check if a given integer is in the list?


def binary_search(num_list, target):
    floor, ceil = 0, len(num_list)
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


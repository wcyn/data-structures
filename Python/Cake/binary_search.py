# https://www.interviewcake.com/concept/python/binary-search?course=fc1&section=sorting-searching-logarithms


def iterative_binary_search(num_list, target):
    floor, ceil = 0, len(num_list) - 1

    while floor <= ceil:
        mid = ceil + ((floor - ceil) // 2)
        print(mid)
        if num_list[mid] == target:
            return mid
        if num_list[mid] > target:
            ceil = mid - 1
        else:
            floor = mid + 1
    return -1


nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(iterative_binary_search(nums, 7))

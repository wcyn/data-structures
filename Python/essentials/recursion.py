def factorial(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial(num-1)

print("5 Factorial: ", factorial(5))

# Binary Search (Non-recursive)

nums = [3, 12, 14, 16, 19, 23]

def binary_search(target, num_list):
    list_len = len(num_list)
    low = 0
    high = list_len - 1
    if list_len < 1:
        return False
    else:
        while low <= high:
            mid = (low + high)// 2
            if num_list[mid] == target:
                return True
            elif num_list[mid] > target:
                high = mid - 1
            else:
                low = mid + 1
    return False

print("Non-recursive binary search", binary_search(23, nums))


def r_binary_search(target, num_list, low, high):
    if len(num_list) == 0:
        return False
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if num_list[mid] == target:
            return True
        elif num_list[mid] > target:
            high = mid - 1
        else:
            low = mid + 1
        return r_binary_search(target, num_list, low, high)

print("Recursive binary search", r_binary_search(23, nums, 0, len(nums) - 1))


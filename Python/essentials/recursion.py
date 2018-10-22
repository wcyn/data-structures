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

def bad_fibonacci(num):
    """O(2^n)"""
    if num <= 1:
        return num
    else:
        return bad_fibonacci(num - 2) + bad_fibonacci(num - 1)

print("Bad Fibonacci: ", bad_fibonacci(4))

def good_fibonacci(num):
    """O(n)"""
    if num <= 1:
        return (num, 0)
    else:
        (a, b) = good_fibonacci(num-1)
        print("a:{} , b:{}".format(a, b))
        return (a+b, a)
print("Good Fibonacci: ", good_fibonacci(4))


def linear_sum(num_list, n):
    if n == 0:
        return 0
    else:
        return linear_sum(num_list, n-1) + num_list[n-1]

nums = [1,2,3,4,5]
print("Linear Sum: ", linear_sum(nums, 5))
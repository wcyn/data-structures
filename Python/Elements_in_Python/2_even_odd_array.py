# Your input is an array of
# integers, and you have to reorder its entries so that the even entries
# appear first
l = [0, 5, 2, 5, 9, 3, 8, 45, 10]
n = [2,3,4,7]

def even_odd(nums):
    left, right = 0, len(nums) - 1
    while left < right:
        if nums[left] % 2 == 0:
            if nums[right] % 2 != 0:
              right -= 1
            left += 1
        else:
            if nums[right] % 2 == 0:
                # swap the two
                nums[right], nums[left] = nums[left], nums[right]
                left += 1
            right -= 1

    return nums

def even_odd_2(A):
    next_even , next_odd = 0, len(A) - 1
    while next_even < next_odd:
        if A[ next_even ] % 2 == 0:
            next_even += 1
        else:
            A[ next_even ], A[next_odd] = A[next_odd], A[ next_even ]
            next_odd -= 1
    return A

print(even_odd(n))
num_list = [0, 0, 78, -8321, 34, 53, 1, 43, 5]
def quick_sort(nums):
    _quick_sort(nums, 0, len(nums) - 1)

def _quick_sort(nums, low, high):
    if low < high:
        p = _partition(nums, low, high)
        _quick_sort(nums, low, p-1)
        _quick_sort(nums, p+1, high)

def _get_pivot(nums, low, high):
    return high

def _partition(nums, low, high):
    pivot_index = _get_pivot(nums, low, high)
    pivot_value = nums[pivot_index]
    # swap highest and pivot
    nums[high], nums[pivot_index] = nums[pivot_index], nums[high]

    border = low
    for i in range(low, high):
        if nums[i] < pivot_value:
            # swap with border
            nums[i], nums[border] = nums[border], nums[i]
            border += 1

    nums[border], nums[high] = nums[high], nums[border]
    print(border)
    return border

n = [3, 20, 7, 8, 72, 4, 19]
quick_sort(num_list)
print(num_list)
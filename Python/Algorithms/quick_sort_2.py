num_list = [54, -430, 53.54, 23, 5, 632, 3, 44, 2, 0]
def quick_sort(nums):
    _quick_sort(nums, 0, len(nums) - 1)

def _quick_sort(nums, start, end):
    if start < end:
        partition = _partition(nums, start, end)
        _quick_sort(nums, start, partition-1)
        _quick_sort(nums, partition+1, end)

def _partition(nums, start, end):
    pivot_index = _get_pivot_index(nums, start, end)
    pivot_value = nums[pivot_index]
    # swap pivot with last element of array
    nums[end], nums[pivot_index] = nums[pivot_index], nums[end]
    partition = start
    for i in range(start, end):
        if nums[i] < pivot_value:
            nums[i], nums[partition] = nums[partition], nums[i]
            partition += 1

    nums[partition], nums[end] = nums[end], nums[partition]
    return partition

def _get_pivot_index(nums, start, end):

    mid = start + (end - start) // 2
    if nums[start] <= nums[end] <= nums[mid] or nums[mid] <= nums[end] <= nums[start]:
        pivot_index = end
    elif nums[end] <= nums[start] <= nums[mid] or nums[mid] <= nums[start] <= nums[end]:
        pivot_index = start
    else:
        pivot_index = mid
    # pivot_index = end
    return pivot_index

quick_sort(num_list)
print(num_list)
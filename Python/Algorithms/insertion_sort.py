num_list = [-1, 0, 4234, -6, 23, 25, 236, 64, 7]
def insertion_sort(nums):
    i_count = 1
    for i in nums:
        if i_count >= len(nums):
            break
        key = nums[i_count]
        j = i_count - 1
        while nums[j] > key and j >= 0:
            nums[j+1] = nums[j]
            j -= 1
        nums[j + 1] = key
        i_count += 1
    return nums

print(insertion_sort(num_list))

num_list = [8, 24, 78, 1, 93, 230, 23, 54]
def bubble_sort(nums):
    i = 0
    for num in nums:
        j = i + 1
        while j < len(nums):
            if nums[i] > nums[j]:
                # swap
                nums[i], nums[j] = nums[j], nums[i]
            j += 1
        i += 1
    return nums

print(bubble_sort(num_list))
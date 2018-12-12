num_list = [5, 23, 64, 1, 467, 7, 22, 53, 23, 9, 0, 31]
def merge_sort_list(nums):
    return merge_sort(nums, 0, len(nums) - 1)

def merge_sort(nums, start, end):
    if end == start:
        return nums[start: end+1]

    mid = start + (end - start)//2
    left_half = merge_sort(nums, start, mid)
    right_half = merge_sort(nums, mid+1, end)
    return merge(left_half, right_half)

def merge(left, right):
    merged = []
    l = r = 0
    while l < len(left) and r < len(right):
        if left[l] > right[r]:
            merged.append(right[r])
            r += 1
        else:
            merged.append(left[l])
            l += 1
    print(merged)

    if l < len(left):
        merged += left[l:]
    elif r < len(right):
        merged += right[r:]
    return merged

# print(merge([3,6,7,9,11], [1,2,3,4,4,13,17, 19]))
print(merge_sort_list(num_list))
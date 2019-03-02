def merge(list1, list2):
    merged_list = [None] * (len(list1) + len(list2))
    merged_pointer = l1_pointer = l2_pointer = 0
    while merged_pointer < len(merged_list):
        # print(merged_pointer, list1[l1_pointer], list2[l2_pointer])
        if l1_pointer >= len(list1):
            while l2_pointer < len(list2):
                merged_list[merged_pointer] = list2[l2_pointer]
                l2_pointer += 1
                merged_pointer += 1
            break
        if l2_pointer >= len(list2):
            while l1_pointer < len(list1):
                merged_list[merged_pointer] = list1[l1_pointer]
                l1_pointer += 1
                merged_pointer += 1
            break
        if list1[l1_pointer] < list2[l2_pointer]:
            merged_list[merged_pointer] = list1[l1_pointer]
            l1_pointer += 1
        else:
            merged_list[merged_pointer] = list2[l2_pointer]
            l2_pointer += 1

        merged_pointer += 1
    return merged_list


# print(merge([1, 5, 7], [3, 4, 23]))


def merge_sort(nums, start, end):
    print start, end
    if end - start == 0:
        return [nums[start]]
    mid = start + (end - start) // 2

    left = merge_sort(nums, start, mid)
    print left
    right = merge_sort(nums, mid+1, end)
    print right, "\n"
    return merge(left, right)


nums = [7, 1, 5, 23, 4, 3]
# print(merge_sort(nums, 0, len(nums)-1))


def generateParenthesis(N):
    ans = []

    def backtrack(S, left, right, node_count):
        # print S, left, right, node_count
        ans.append(S)
        node_count += 1
        if len(S) == 2 * N:
            # leaf_count += 1
            # ans.append(S)
            # print("S")
            return
        backtrack(S + '(', left + 1, right, node_count)
        backtrack(S + ')', left, right + 1, node_count)

    backtrack('', 0, 0, 0)
    return ans


ans = generateParenthesis(3)
print ans, "\n", len(ans)

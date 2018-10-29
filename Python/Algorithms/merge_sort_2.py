def merge_sort(num_list):
    list_len = len(num_list)
    m = _merge_sort(num_list, 0, list_len)
    return m

def _merge_sort(num_list, start, end):
    if end - start <1:
        # print(f"Sorted: {num_list[start:end+1]}" )
        return num_list[start:end+1]
    mid = (start + end) // 2
    S1 = _merge_sort(num_list, start, mid)
    S2 = _merge_sort(num_list, mid + 1, end)

    # print(f"Merging...: S1: {S1}, S2: {S2}, ")
    return _merge(S1, S2)

def _merge(l1, l2):
    S = []
    l1_count = l2_count = 0
    while l1_count < len(l1) and l2_count < len(l2):
        if l1[l1_count] < l2[l2_count]:
            S.append(l1[l1_count])
            l1_count += 1
        else:
            S.append(l2[l2_count])
            l2_count += 1

    if l1_count < len(l1):
        S += l1[l1_count:]
    elif l2_count < len(l2):
        S += l2[l2_count:]
    print(S)
    return S

# print(_merge([3,6,7,9,11], [1,2,3,4,4,13,17, 19]))
print(merge_sort([5,1,7,12,3,56,1,4,89,65,4,32,54]))
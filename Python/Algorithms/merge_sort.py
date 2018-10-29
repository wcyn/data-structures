def merge(S1, S2, S):
    """
    Merge two sorted lists S1 and S2 into list S
    """
    print(f"Merging... S1: {S1}, S2: {S2}, S: {S}")
    i = j = 0
    while i + j < len(S):
        if j == len(S2) or (i < len(S1) and S1[i] < S2[j]):
            # copy ith element of S1 as next item of S
            S[i+j] = S1[i]
            i += 1
        else:
            S[i+j] = S2[j]
            j += 1
    print(f"Merged:{S}\n")

def merge_sort(S):
    n = len(S)
    if n < 2:
        # List already sorted
        return

    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]

    print(f"Before MS1: {S1}")
    merge_sort(S1)
    print(f"Before MS2: {S2}")
    merge_sort(S2)

    merge(S1, S2, S)

# print(merge_sort([54,23,87,1,13,57,23,86,13,64,1]))[]


def merge_sort2(S):
    n = len(S)
    mid = n // 2
    S1 = S[:mid]
    S2 = S[mid:]

    merge_sort(S1)
    merge_sort(S2)

    merge(S1, S2, S)

l = [3,2,1,4, 7, 9, 8, 30]
merge_sort2(l)
print(f"Sorted: {l}")
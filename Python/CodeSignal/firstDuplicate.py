def firstDuplicate(A):
    for x in A:
        A[abs(x) - 1] *= -1
        if A[abs(x) - 1] > 0:
            return abs(x)
    return -1

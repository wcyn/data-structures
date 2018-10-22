# Given a sequence S consisting of n numbers,
# we want to compute a sequence A such that A[j] is the average of elements
# S[0], . . . ,S[ j], for j = 0, . . . ,n−1,

def prefix_average(S):
    # O(n^2)
    n = len(S) # O(1)
    A = [0] * n # Initialize array with zeros O(n)
    count = 0

    for i in range(n):
        for j in range(i+1):
            count += 1
            A[i] += S[j]
        A[i] /= i+1

    return A, count

S = [1,2,3,4,5,6]

print("Quadratic time prefix average: \nResults: {}\nIterations: {}\n".format(
*prefix_average(S)))

def linear_prefix_average(S):
    # O(n)
    n = len(S) # O(1)
    current_total = 0 # O(1)
    A = [] # O(1)
    count = 0
    for i in range(n):
        current_total += S[i]
        A.append((current_total) / (i+1))
        count += 1
    return A, count

print("\nLinear time prefix average: \nResults: {}\nIterations: {}\n".format(
*linear_prefix_average(S)))

### Three way set disjointness

def disjoint1(A, B, C):
    """
    O(A*B*C) n^3 if lengths are equal
    Check if there is no common element in A, B and C. Reeturn True
    if no element is found belonging to all 3
    """
    count = 0
    for a in A:
        for b in B:
            for c in C:
                count += 1
                if a == b == c:
                    return False, count
    return True, count

A = [1,2,3,4,15]
B = [11,12,13,14,15]
C = [21,22,23,24,25]

print("Inefficient Disjoint: \nResults: {}\nIterations: {}\n".format(
    *disjoint1(A, B, C)))

def efficient_disjoint(A, B, C):
    """
    O(n^2)
    """
    count = 0
    for a in A:
        for b in B:
            count += 1
            if a == b:
                for c in C:
                    count += 1
                    if a == c:
                        return False, count
    return True, count


print("More Efficient Disjoint: \nResults: {}\nIterations: {}\n".format(
    *efficient_disjoint(A, B, C)))
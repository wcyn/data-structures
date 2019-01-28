# https://www.interviewcake.com/question/python/find-duplicate-optimize-for-space-beast-mode?course=fc1&section=trees-graphs
# In Find a duplicate, Space Edition™, we were given a list of integers where:

# the integers are in the range 1..n
# the list has a length of n+1
# These properties mean the list must have at least 1 duplicate. Our challenge was to find a duplicate number,
# while optimizing for space. We used a divide and conquer approach, iteratively cutting the
# list in half to find a duplicate integer in O(nlgn) time and O(1) space (sort of a modified binary search).
#
# But we can actually do better. We can find a duplicate integer in O(n) time while keeping our space cost atO(1).
#
# This is a tricky one to derive (unless you have a strong background in graph theory), so we'll get you started:
#
# Imagine each item in the list as a node in a linked list.
# In any linked list, ↴ each node has a value and a "next" pointer. In this case:
#
# The value is the integer from the list.
# The "next" pointer points to the value-eth node in the list
# (numbered starting from 1). For example, if our value was 3, the "next" node would be the third node.

nums = [1, 4, 3, 2, 3]
n2 = [1, 3, 2, 4, 2]
n3 = [1, 3, 4, 1, 2]


def find_duplicate(num_list):
    # get into cycle
    current_position = num_list[-1]  # Head of the linked list
    for _ in range(len(num_list) - 1):
        current_position = num_list[current_position-1]

    # Get length of cycle. Remember the current position then count the steps it takes to get back
    cycle_position = num_list[current_position-1]
    cycle_length = 1
    while cycle_position != current_position:
        cycle_position = num_list[cycle_position-1]
        cycle_length += 1

    # Get cycle start and end
    cycle_start = cycle_end = num_list[-1]
    for _ in range(cycle_length):
        cycle_start = num_list[cycle_start-1]

    while cycle_start != cycle_end:
        cycle_start = num_list[cycle_start-1]
        cycle_end = num_list[cycle_end-1]

    return cycle_start


print(find_duplicate(nums))
print(find_duplicate(n2))
print(find_duplicate(n3))




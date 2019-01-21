# Find a duplicate, Space Edition™.
# We have a list of integers, where:
#
# The integers are in the range 1..n1..n
# The list has a length of n+1n+1
# It follows that our list has at least one integer which appears at least twice.
# But it may have several duplicates, and each duplicate may appear more than twice.
#
# Write a function which finds an integer that appears more than once in our list.
# (If there are multiple duplicates, you only need to find one of them.)
#
# We're going to run this function on our new, super-hip MacBook Pro With Retina Display™.
# Thing is, the damn thing came with the RAM soldered right to the motherboard,
# so we can't upgrade our RAM. So we need to optimize for space!


def find_a_duplicate(num_list):
    current_index = 0
    iters = 0
    while current_index < len(num_list):
        iters += 1
        current_num = num_list[current_index]
        if current_num == current_index + 1:
            current_index += 1
        else:
            # We need to swap this num to the right place
            # First check if it already exists at that index
            if current_num == num_list[current_num-1]:
                return current_num
            else:
                # Swap em
                num_list[current_index], num_list[current_num-1] = num_list[current_num-1], num_list[current_index]
    # print(iters)
    return None


def find_repeat(the_list):
    floor = 1
    ceiling = len(the_list) - 1

    while floor < ceiling:
        # Divide our range 1..n into an upper range and lower range
        # (such that they don't overlap)
        # Lower range is floor..midpoint
        # Upper range is midpoint+1..ceiling
        midpoint = floor + ((ceiling - floor) // 2)
        lower_range_floor, lower_range_ceiling = floor, midpoint
        upper_range_floor, upper_range_ceiling = midpoint + 1, ceiling

        # Count number of items in lower range
        items_in_lower_range = 0
        for item in the_list:
            # Is it in the lower range?
            if item >= lower_range_floor and item <= lower_range_ceiling:
                items_in_lower_range += 1

        distinct_possible_integers_in_lower_range = (
                lower_range_ceiling
                - lower_range_floor
                + 1
        )
        if items_in_lower_range > distinct_possible_integers_in_lower_range:
            # There must be a duplicate in the lower range
            # so use the same approach iteratively on that range
            floor, ceiling = lower_range_floor, lower_range_ceiling
        else:
            # There must be a duplicate in the upper range
            # so use the same approach iteratively on that range
            floor, ceiling = upper_range_floor, upper_range_ceiling

    # Floor and ceiling have converged
    # We found a number that repeats!
    return floor


nums = [1, 1, 3, 2, 4]
n = [3, 5, 7, 2, 4, 6, 1]
print(find_a_duplicate(nums))
print(nums)

print(find_repeat(nums))

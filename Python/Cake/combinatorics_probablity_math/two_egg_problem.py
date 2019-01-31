# https://www.interviewcake.com/question/python/two-egg-problem?course=fc1&section=combinatorics-probability-math
# A building has 100 floors. One of the floors is the highest floor an egg can be dropped from without breaking.
#
# If an egg is dropped from above that floor, it will break.
# If it is dropped from that floor or below, it will be completely undamaged and you can drop the egg again.
#
# Given two eggs, find the highest floor an egg can be dropped from without breaking, with as few drops as possible.
import math


def get_highest_non_breaking_floor(total_number_of_floors):
    step_size = int(math.sqrt(total_number_of_floors))
    breaks_at = 78
    egg1 = 0

    for step in range(1, step_size+1):
        # print(egg1)
        if egg1 > breaks_at:
            break
        egg1 += step_size

    start_floor = egg1 - step_size
    egg2 = start_floor
    # print(egg2)
    while egg2 != breaks_at:
        egg2 += 1

    return egg2


# print(get_highest_non_breaking_floor(100))


def get_highest_non_breaking_floor_series(total_number_of_floors):
    # triangular series formula = (n^2 - n)/ 2 = total_number_of_floors
    initial_step_size_a = (-1 + (math.sqrt(1 - (4 * (-2 * total_number_of_floors))))) / 2
    initial_step_size_b = (-1 - (math.sqrt(1 - (4 * (-2 * total_number_of_floors))))) / 2

    initial_step_size = math.ceil(max(initial_step_size_a, initial_step_size_b))
    breaks_at = 78
    egg1 = initial_step_size
    print(initial_step_size)
    previous_step_size = 1
    while egg1 < breaks_at:
        print(egg1)
        previous_step_size = egg1
        egg1 += egg1 - 1

    egg2 = previous_step_size
    # print(egg2)
    while egg2 != breaks_at:
        egg2 += 1

    return egg2


print(get_highest_non_breaking_floor_series(100))


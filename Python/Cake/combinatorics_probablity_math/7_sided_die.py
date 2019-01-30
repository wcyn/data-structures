# https://www.interviewcake.com/question/python/simulate-7-sided-die?course=fc1&section=combinatorics-probability-math
# You have a function rand5() that generates a random integer from 1 to 5.
# Use it to write a function rand7() that generates a random integer from 1 to 7.
#
# rand5() returns each integer with equal probability.
# rand7() must also return each integer with equal probability.

import random


def rand5():
    return random.randrange(1, 6)


def rand7():
    mapping = {
        (1, 1): 1,
        (2, 2): 2,
        (3, 3): 3,
        (4, 4): 4,
        (5, 5): 5,
        (1, 2): 6,
        (1, 3): 7,
    }
    rand_int_1 = rand5()
    rand_int_2 = rand5()
    while (rand_int_1, rand_int_2) not in mapping:
        rand_int_1 = rand5()
        rand_int_2 = rand5()
    return mapping[(rand_int_1, rand_int_2)]


def rand7_2():
    # Like using base 5
    while True:
        rand_int_1 = rand5()
        rand_int_2 = rand5()
        outcome = ((rand_int_1 - 1) * 5) + ((rand_int_2 - 1) + 1)
        if outcome > 21:
            continue
        return outcome % 7 + 1


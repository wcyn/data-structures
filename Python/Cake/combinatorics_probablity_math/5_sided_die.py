# https://www.interviewcake.com/question/python/simulate-5-sided-die?course=fc1&section=combinatorics-probability-math
#  You have a function rand7() that generates a random integer from 1 to 7.
# Use it to write a function rand5() that generates a random integer from 1 to 5.
#
# rand7() returns each integer with equal probability.
# rand5() must also return each integer with equal probability.

import random


def rand_7():
    return random.randrange(1, 8)


def simulate_rand_5():
    rand_int = rand_7()
    while rand_int > 5:
        rand_int = rand_7()
    return rand_int


print(simulate_rand_5())


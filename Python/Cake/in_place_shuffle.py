# https://www.interviewcake.com/question/python/shuffle?course=fc1&section=greedy
# Write a function for doing an in-place shuffle of a list.
import random


def do_in_place_shuffle(num_list):

    for index in range(0, len(num_list) - 1):
        random_index = random.randrange(index, len(num_list))
        num_list[index], num_list[random_index] = num_list[random_index], num_list[index]


nums = [1, 2, 3, 4, 5, 6]
do_in_place_shuffle(nums)
print(nums)

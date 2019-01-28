# https://www.interviewcake.com/question/python/coin?course=fc1&section=dynamic-programming-recursion
# Your quirky boss collects rare, old coins...
# They found out you're a programmer and asked you to solve something they've been wondering for a long time.
#
# Write a function that, given:
# - an amount of money
# - a list of coin denominations
# computes the number of ways to make the amount of money with coins of the available denominations.
#
# Example: for amount=4 (4¢) and denominations=[1,2,3](1¢, 2¢ and 3¢), your program would output 4—
# the number of ways to make 4¢ with those denominations:
#
# - 1¢, 1¢, 1¢, 1¢
# - 1¢, 1¢, 2¢
# - 1¢, 3¢
# - 2¢, 2¢


def get_change(amount, denominations, denomination_index=0):
    if amount == 0:
        return [denominations[denomination_index]]

    elif amount < 0:
        return [-1]

    coins = []
    for index, denomination in enumerate(denominations):
        new_amount = amount - denomination
        current_change = get_change(new_amount, denominations, index)
        for change in current_change:
            coins.append(change)

    return coins


print(get_change(4, [1, 2, 3, 4]))


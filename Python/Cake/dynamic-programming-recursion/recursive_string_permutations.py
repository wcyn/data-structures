# https://www.interviewcake.com/question/python/recursive-string-permutations?course=fc1&section=dynamic-programming-recursion
# Write a recursive function for generating all permutations of an input string. Return them as a set.
#
# Don't worry about time or space complexity—if we wanted efficiency we'd write an iterative version.
#
# To start, assume every character in the input string is unique.
#
# Your function can have loops—it just needs to also be recursive.

chars = "abcd"


def generate_all_permutations(chars):
    if len(chars) <= 1:
        # permutations ^= {tuple(chars)}
        return set(chars)

    all_chars_except_last = chars[:-1]
    last_char = chars[-1]

    # Recursive call: Get all possible permutations for all chars except the last
    permutations_of_all_chars_except_last = generate_all_permutations(all_chars_except_last)

    # Put the last char in all possible positions for each of the above permutations

    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(all_chars_except_last) + 1):
            permutation = (
                permutation_of_all_chars_except_last[:position] +
                last_char +
                permutation_of_all_chars_except_last[position:]

            )
            print("Perm: ", permutation)
            permutations.add(permutation)
    print("Permutations: ", permutations)
    return permutations


perms = {(chars[0],)}
print(generate_all_permutations(chars))

print(perms)


def generate_all_permutations_2(chars):
    if len(chars) <= 1:
        return set(chars)

    all_chars_except_last = chars[:-1]
    last_char = chars[-1]

    permutations_of_all_chars_except_last = generate_all_permutations(all_chars_except_last)
    permutations = set()
    for permutation_of_all_chars_except_last in permutations_of_all_chars_except_last:
        for position in range(len(chars)):
            permutation = (
                permutation_of_all_chars_except_last[:position]
                + last_char
                + permutation_of_all_chars_except_last[position:]
            )
            permutations.add(permutation)

    return permutations

print(generate_all_permutations_2("xyz"))

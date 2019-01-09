# https://www.interviewcake.com/question/python/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
# Write an efficient function that checks whether any permutation of an input string is a palindrome.


def permutation_is_palindrome(chars):
    char_counts = {}
    for char in chars:
        if char in char_counts:
            char_counts[char] = not char_counts[char]
        else:
            char_counts[char] = False

    odd = False
    for count in char_counts.values():
        if not count:
            if odd:
                return False
            odd = True
    return True


def permutation_is_palindrome_2(chars):
    char_set = set()
    for char in chars:
        if char in char_set:
            char_set.remove(char)
        else:
            char_set.add(char)

    return len(char_set) < 2


print(permutation_is_palindrome_2('ldfsldfse'))

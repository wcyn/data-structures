# https://www.interviewcake.com/question/python/permutation-palindrome?course=fc1&section=hashing-and-hash-tables
# Write an efficient function that checks whether any permutation of an input string is a palindrome.
import unittest

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


# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)
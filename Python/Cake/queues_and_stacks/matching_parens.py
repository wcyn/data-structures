# https://www.interviewcake.com/question/python/matching-parens?course=fc1&section=queues-stacks
# I like parentheticals (a lot).
# "Sometimes (when I nest them (my parentheticals) too much (like this (and this))) they get confusing."
#
# Write a function that, given a sentence like the one above,
# along with the position of an opening parenthesis, finds the corresponding closing parenthesis.
#
# Example: if the example string above is input with the number 10
# (position of the first parenthesis), the output should be 79 (position of the last parenthesis).
import unittest


def get_closing_paren(sentence, opening_paren_index):
    paren_stack = []
    char_index = opening_paren_index
    while char_index < len(sentence):
        if sentence[char_index] == "(":
            paren_stack.append("(")
        elif sentence[char_index] == ")":
            # Check if there's only one paren in the stack
            if len(paren_stack) == 1:
                return char_index
            elif len(paren_stack) > 1:
                paren_stack.pop()
            else:
                raise Exception("Invalid Parenthesis Structure")
        char_index += 1
    raise Exception("Invalid Parenthesis Structure")


def get_closing_paren_constant_space(sentence, opening_paren_index):
    opening_parens = 0
    char_index = opening_paren_index
    while char_index < len(sentence):
        if sentence[char_index] == "(":
            opening_parens += 1
        elif sentence[char_index] == ")":
            opening_parens -= 1
            if opening_parens == 0:
                return char_index
        char_index += 1
    raise Exception("No closing Parens")


sentence = "Sometimes (when I nest them (my parentheticals() too much (like this (and this))) they get confusing."
# print(get_closing_paren(sentence, 1))
print(get_closing_paren_constant_space(sentence, 1))


class Test(unittest.TestCase):

    def test_all_openers_then_closers(self):
        actual = get_closing_paren('((((()))))', 2)
        expected = 7
        self.assertEqual(actual, expected)

    def test_mixed_openers_and_closers(self):
        actual = get_closing_paren('()()((()()))', 5)
        expected = 10
        self.assertEqual(actual, expected)

    def test_no_matching_closer(self):
        with self.assertRaises(Exception):
            get_closing_paren('()(()', 2)


unittest.main(verbosity=2)

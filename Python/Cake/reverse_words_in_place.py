# https://www.interviewcake.com/question/python/reverse-words?course=fc1&section=array-and-string-manipulation

# Write a function reverse_words() that takes a message as a list of characters
# and reverses the order of the words in place

message = [
    'c', 'a', 'k', 'e', '!', ' ',
    'p', 'o', 'u', 'n', 'd', ' ',
    's', 't', 'e', 'a', 'l']


# def reverse_words(words):
#     left, right = 0, len(words)-1
#     space_indexes = [len(words)]
#     while left < right:
#         words[right], words[left] = words[left], words[right]
#         if words[right] == ' ':
#             space_indexes.append(right)
#         elif words[left] == ' ':
#             space_indexes.append(left)
#         left += 1
#         right -= 1
#     space_indexes.append(-1)
#     print(space_indexes)
#     print(words)
#     correct_words(words, space_indexes)
#
#
# def correct_words(words, space_indexes):
#     index = 0
#     while index < len(space_indexes) - 1:
#         left, right = space_indexes[index+1]+1, space_indexes[index]-1
#         while left < right:
#             words[right], words[left] = words[left], words[right]
#             left += 1
#             right -= 1
#         index += 1


def reverse_words(words):
    reverse_characters(words, 0, len(words)-1)
    left = 0
    for index in range(len(words) + 1):
        if index == len(words) or words[index] == ' ':
            right = index - 1
            reverse_characters(words, left, right)
            left = index + 1


def reverse_characters(words, left, right):
    while left < right:
        words[left], words[right] = words[right], words[left]
        left += 1
        right -= 1


reverse_words(message)
print(message)


# Tests

class Test(unittest.TestCase):

    def test_one_word(self):
        message = list('vault')
        reverse_words(message)
        expected = list('vault')
        self.assertEqual(message, expected)

    def test_two_words(self):
        message = list('thief cake')
        reverse_words(message)
        expected = list('cake thief')
        self.assertEqual(message, expected)

    def test_three_words(self):
        message = list('one another get')
        reverse_words(message)
        expected = list('get another one')
        self.assertEqual(message, expected)

    def test_multiple_words_same_length(self):
        message = list('rat the ate cat the')
        reverse_words(message)
        expected = list('the cat ate the rat')
        self.assertEqual(message, expected)

    def test_multiple_words_different_lengths(self):
        message = list('yummy is cake bundt chocolate')
        reverse_words(message)
        expected = list('chocolate bundt cake is yummy')
        self.assertEqual(message, expected)

    def test_empty_string(self):
        message = list('')
        reverse_words(message)
        expected = list('')
        self.assertEqual(message, expected)


unittest.main(verbosity=2)
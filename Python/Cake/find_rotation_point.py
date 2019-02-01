# https://www.interviewcake.com/question/python/find-rotation-point?course=fc1&section=sorting-searching-logarithms
# Write a function for finding the index of the "rotation point,"
import unittest
def find_rotation_point(word_list):
    if not word_list:
        return None
    floor, ceil = 0, len(word_list) - 1

    while floor <= ceil:
        mid = floor + ((ceil - floor) // 2)
        if word_list[mid-1] > word_list[mid]:
            return mid
        if word_list[0] > word_list[mid]:
            ceil = mid - 1
        else:
            floor = mid + 1
    return -1


words = [
    'ptolemaic',
    'retrograde',
    'supplant',
    'undulate',
    'xenoepist',
    'asymptote',  # <-- rotates here!
    'babka',
    'banoffee',
    'engender',
    'karpatka',
    'othellolagkage',
]
w = ['a']
print(find_rotation_point(w))


# Tests

class Test(unittest.TestCase):

    def test_small_list(self):
        actual = find_rotation_point(['cape', 'cake'])
        expected = 1
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_rotation_point(['grape', 'orange', 'plum',
                                      'radish', 'apple'])
        expected = 4
        self.assertEqual(actual, expected)

    def test_large_list(self):
        actual = find_rotation_point(['ptolemaic', 'retrograde', 'supplant',
                                      'undulate', 'xenoepist', 'asymptote',
                                      'babka', 'banoffee', 'engender',
                                      'karpatka', 'othellolagkage'])
        expected = 5
        self.assertEqual(actual, expected)

    # Are we missing any edge cases?


unittest.main(verbosity=2)
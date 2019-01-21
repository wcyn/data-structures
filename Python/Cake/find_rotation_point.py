# https://www.interviewcake.com/question/python/find-rotation-point?course=fc1&section=sorting-searching-logarithms
# Write a function for finding the index of the "rotation point,"


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

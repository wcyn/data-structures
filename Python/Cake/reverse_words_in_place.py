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

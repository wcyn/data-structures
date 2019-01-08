# https://www.interviewcake.com/question/python/reverse-string-in-place?course=fc1&section=array-and-string-manipulation
# Write a function that takes a list of characters and reverses the letters in place.


def reverse_in_place(chars):
    left, right = 0, len(chars) - 1
    while left < right:
        swap_chars(left, right, chars)
        left += 1
        right -= 1


def swap_chars(left, right, chars):
    # chars[left], chars[right] = chars[right], chars[left]
    tmp = chars[left]
    chars[left] = chars[right]
    chars[right] = tmp


str_chars = list('Hello')
reverse_in_place(str_chars)

print(str_chars)

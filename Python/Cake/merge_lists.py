# https://www.interviewcake.com/question/python/merge-sorted-arrays?course=fc1&section=array-and-string-manipulation
# Write a function to merge our lists of orders into one sorted list.

my_list = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]


def merge_lists(list1, list2):
    merged_list = []
    list1_ptr = list2_ptr = 0
    while list1_ptr < len(list1) and list2_ptr < len(list2):
        if list1[list1_ptr] < list2[list2_ptr]:
            merged_list.append(list1[list1_ptr])
            list1_ptr += 1
        elif list1[list1_ptr] > list2[list2_ptr]:
            merged_list.append(list2[list2_ptr])
            list2_ptr += 1
        else:
            merged_list.append(list1[list1_ptr])
            list1_ptr += 1
            list2_ptr += 1

    while list1_ptr < len(list1):
        merged_list.append(list1[list1_ptr])
        list1_ptr += 1
    while list2_ptr < len(list2):
        merged_list.append(list2[list2_ptr])
        list2_ptr += 1

    return merged_list


print(merge_lists(my_list, alices_list))

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
Given a sorted array nums, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example 1:

Given nums = [1,1,2],

Your function should return length = 2, with the first two elements of nums being 1 and 2 respectively.

It doesn't matter what you leave beyond the returned length.
"""

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        num_count = 0
        if not nums:
            return num_count

        current_num_and_index = None, -1
        for num in nums:
            if num != current_num_and_index[0]:
                new_index = current_num_and_index[1] + 1
                nums[new_index] = num
                current_num_and_index = num, new_index
                num_count += 1
        return num_count

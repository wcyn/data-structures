"""
https://leetcode.com/problems/remove-element/
Given an array nums and a value val, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example 1:

Given nums = [3,2,2,3], val = 3,

Your function should return length = 2, with the first two elements of nums being 2.

It doesn't matter what you leave beyond the returned length.
"""

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if not nums:
            return 0

        start_pointer, end_pointer = 0, len(nums) - 1
        while start_pointer <= end_pointer:
            if nums[start_pointer] == val:
                if nums[end_pointer] == val:
                    end_pointer -= 1
                else:
                    nums[end_pointer], nums[start_pointer] = nums[start_pointer], nums[end_pointer]
                    end_pointer -= 1
                    start_pointer += 1
            else:
                start_pointer += 1

        return start_pointer




"""
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
Given an array of integers nums sorted in ascending order,
find the starting and ending position of a given target value.

Your algorithm's runtime complexity must be in the order of O(log n).

If the target is not found in the array, return [-1, -1].

Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
"""


class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        def get_start_index(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    if mid == 0 or nums[mid - 1] != target:
                        return mid
                if nums[mid] < target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        def get_end_index(nums, target):
            start, end = 0, len(nums) - 1
            while start <= end:
                mid = start + (end - start) // 2
                if nums[mid] == target:
                    if mid == len(nums) - 1 or nums[mid + 1] != target:
                        return mid
                if nums[mid] <= target:
                    start = mid + 1
                else:
                    end = mid - 1
            return -1

        return [get_start_index(nums, target), get_end_index(nums, target)]

"""
https://leetcode.com/problems/3sum-closest/
Given an array nums of n integers and an integer target,
find three integers in nums such that the sum is closest to target.
Return the sum of the three integers. You may assume that each input would have exactly one solution.

Example:

Given array nums = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
"""


class Solution:
    def threeSumClosest_2(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums) < 3:
            return []

        closest_sum = nums[0] + nums[1] + nums[2]
        min_difference = abs(closest_sum - target)
        for first_index in range(0, len(nums) - 2):
            for second_index in range(first_index + 1, len(nums) - 1):
                for third_index in range(second_index + 1, len(nums)):
                    current_sum = nums[first_index] + nums[second_index] + nums[third_index]
                    current_difference = abs(current_sum - target)
                    if min_difference > current_difference:
                        min_difference = current_difference
                        closest_sum = current_sum
        return closest_sum

    def threeSumClosest(self, nums: 'List[int]', target: 'int') -> 'int':
        if len(nums) < 3:
            return []

        nums.sort()
        closest_sum = nums[0] + nums[1] + nums[2]

        for index in range(0, len(nums) - 2):
            start = index + 1
            end = len(nums) - 1
            while start < end:
                current_sum = nums[index] + nums[start] + nums[end]
                if current_sum > target:
                    end -= 1
                else:
                    start += 1
                if abs(closest_sum - target) > abs(current_sum - target):
                    closest_sum = current_sum
        return closest_sum

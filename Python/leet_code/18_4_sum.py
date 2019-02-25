# https://leetcode.com/problems/4sum/
# Given an array nums of n integers and an integer target,
# are there elements a, b, c, and d in nums such that a + b + c + d = target?
# Find all unique quadruplets in the array which gives the sum of target.
# Note: The solution set must not contain duplicate quadruplets.

# Example:
#
# Given array nums = [1, 0, -1, 0, -2, 2], and target = 0.
#
# A solution set is:
# [
#   [-1,  0, 0, 1],
#   [-2, -1, 1, 2],
#   [-2,  0, 0, 2]
# ]

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        if not nums or target is None:
            return []

        quadruplets = []
        nums.sort()
        for first_index in range(0, len(nums) - 3):
            for second_index in range(first_index + 1, len(nums) - 2):
                start, end = second_index + 1, len(nums) - 1

                while start < end:
                    nums_sum = nums[first_index] + nums[second_index] + nums[start] + nums[end]
                    if nums_sum == target:
                        nums_tuple = [nums[first_index], nums[second_index], nums[start], nums[end]]
                        if nums_tuple not in quadruplets:
                            # print("Nums: ", nums[first_index], nums[second_index], nums[start], nums[end])
                            quadruplets.append(nums_tuple)
                            break
                    if nums_sum < target:
                        start += 1
                    else:
                        end -= 1
        return quadruplets

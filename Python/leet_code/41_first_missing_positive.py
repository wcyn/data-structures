"""
Given an unsorted integer array, find the smallest missing positive integer.

Example 1:

Input: [1,2,0]
Output: 3
Example 2:

Input: [3,4,-1,1]
Output: 2
Example 3:

Input: [7,8,9,11,12]
Output: 1
Note:

Your algorithm should run in O(n) time and uses constant extra space.

"""


class Solution(object):
    # Not constant space
    def firstMissingPositive2(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.sort()
        result = 1
        for num in nums:
            if num == result:
                result += 1
            elif num > result:
                break
        return result

    # Not constant space
    def firstMissingPositive3(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_set = {num for num in nums if num > 0 and num <= len(nums)}
        # print nums_set
        result = 1
        while True:
            if result not in nums_set:
                return result
            result += 1

    # Constant space and linear time
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
         Basic idea:
        1. for any array whose length is l, the first missing positive must be in range [1,...,l+1],
            so we only have to care about those elements in this range and remove the rest.
        2. we can use the array index as the hash to restore the frequency of each number within
             the range [1,...,l+1]
        """
        nums.append(0)
        n = len(nums)
        for i in range(len(nums)):  # delete those useless elements
            if nums[i] < 0 or nums[i] >= n:
                nums[i] = 0
        for i in range(len(nums)):  # use the index as the hash to record the frequency of each number
            print i, nums
            nums[nums[i] % n] += n
            print nums, "\n"
        for i in range(1, len(nums)):
            if nums[i] / n == 0:
                return i
        return n

    def firstMissingPositiveSimpler(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums.append(0)
        num_len = len(nums)
        for num_index in range(num_len):
            if nums[num_index] < 1 or nums[num_index] >= num_len:
                nums[num_index] = 0
        for num_index in range(num_len):
            nums[nums[num_index] % num_len] += num_len

        for num_index in range(1, num_len):
            if nums[num_index] < num_len:
                return num_index
        return num_len

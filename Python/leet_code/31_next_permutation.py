"""
https://leetcode.com/problems/next-permutation/
Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 -> 1,3,2
3,2,1 -> 1,2,3
1,1,5 ->  1,5,1

"""


class Solution(object):

    def nextPermutation1(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        previous_number = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] < previous_number:
                for position in range(index + 1, len(nums)):
                    if nums[position] <= nums[index]:
                        nums[position - 1], nums[index] = nums[index], nums[position - 1]
                        break
                    if position == len(nums) - 1:
                        nums[position], nums[index] = nums[index], nums[position]
                start, end = index + 1, len(nums) - 1
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                return
            previous_number = nums[index]

        start_pointer, end_pointer = 0, len(nums) - 1
        while start_pointer < end_pointer:
            nums[start_pointer], nums[end_pointer] = nums[end_pointer], nums[start_pointer]
            start_pointer += 1
            end_pointer -= 1

    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        if len(nums) < 2:
            return

        def get_next_larger_number_index(index, nums):
            next_larger_number_index = len(nums) - 1
            for position in range(index + 1, len(nums)):
                if nums[position] <= nums[index]:
                    next_larger_number_index = position - 1
                    break
            return next_larger_number_index

        def reverse_num_list(start_index, nums):
            start, end = start_index, len(nums) - 1
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        previous_number = nums[-1]
        for index in range(len(nums) - 2, -1, -1):
            if nums[index] < previous_number:
                swap_index = get_next_larger_number_index(index, nums)
                nums[index], nums[swap_index] = nums[swap_index], nums[index]
                reverse_num_list(index + 1, nums)
                return
            previous_number = nums[index]

        reverse_num_list(0, nums)

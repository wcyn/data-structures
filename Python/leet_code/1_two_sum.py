class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        complements = {}
        for i, val in enumerate(nums):
            comp = target - val
            if comp in complements:
                return [complements[comp], i]
            complements[val] = i
        return None

sol = Solution()
num_list = [2,7,11,15]
print(sol.twoSum(num_list, 9))
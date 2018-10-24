# https://leetcode.com/problems/add-digits/description/
class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        def get_sum(n):
            """~ O(N)"""
            num_sum = n
            while num_sum > 9:
                s = 0
                for i in str(num_sum):
                    s += int(i)
                num_sum = s
            return num_sum

        def get_sum_2(n):
            """O(1)"""
            if n == 0:
                return 0
            return 1 + ((n-1) % 9)

        return get_sum_2(num)

sol = Solution()
print(sol.addDigits(38))
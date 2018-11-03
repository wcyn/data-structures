# https://leetcode.com/problems/palindrome-number/
class Solution:
    def isPalindromeString(self, x):
        """
        :type x: int
        :rtype: bool
        """
        if x < 0:
            return False
        x_str = str(x)

        for i in range(len(x_str)//2):
            if x_str[i] != x_str[-i-1]:
                return False
        return True

    def isPalindrome1(self, x):
        if x < 0:
            return False
        x_list = []
        while x != 0:
            x_list.append(x % 10)
            x //= 10
        for i in range(len(x_list)):
            if x_list[i] != x_list[-i-1]:
                return False
        return True

    def isPalindrome(self, x):
        if x < 0 or (x % 10 == 0 and x != 0):
            return False

        reverted_num = 0
        while x > reverted_num:
            reverted_num = reverted_num * 10 + (x % 10)
            x //= 10

        return x == reverted_num or x == reverted_num // 10

sol = Solution()
print(sol.isPalindrome(2153443512))

# https://leetcode.com/problems/reverse-integer/
class Solution:
    def reverse_2(self, x):
        """
        :type x: int
        :rtype: int
        """
        def check_within_range(x):
            if x < low_range or x > high_range:
                return 0
            return x

        low_range = -2 ** 31
        high_range = (2 ** 31) - 1
        check_within_range(x)

        s_int = list(str(x))
        if s_int[0] == '-':
            result = '-'
            s_int = s_int[1:]
        else:
            result = ''

        while s_int:
            result += s_int.pop()

        return check_within_range(int(result))

    def reverse(self, x):
        def within_range(x):
            low_range = -2 ** 31
            high_range = (2 ** 31) - 1
            if x < low_range or x > high_range:
                return False
            return True
        sign = [1, -1][x<0]
        x *= sign # make absolute
        reverse = 0
        while x != 0:
            reverse *= 10
            reverse += x % 10
            x //= 10
        reverse *= sign
        if not within_range(reverse):
            return 0
        return reverse

sol = Solution()
print(sol.reverse(-46542451))
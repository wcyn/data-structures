# https://leetcode.com/problems/string-to-integer-atoi/
class Solution:
    def myAtoi1(self, s):
        """
        :type str: str
        :rtype: int
        """

        char_list = s.split()
        if not len(char_list): return 0
        char_list = char_list[0]
        min_range = -2 ** 31
        max_range = (2 ** 31) - 1

        res = 0
        sign = 1
        if char_list[0] == '-':
            sign = -1
            char_list = char_list[1:]
        elif char_list[0] == '+':
            char_list = char_list[1:]

        # char_list = char_list[1:]
        # int_found = False
        for char in char_list:
            try:
                res *= 10
                res += int(char)
                int_found = True
            except Exception:
                res //= 10
                break

        res *= sign
        if res < min_range:
                return min_range
        elif res > max_range:
            return max_range
        return res

    def myAtoi2(self, s):
        """
        :type str: str
        :rtype: int
        """
        char_list = s.split()
        min_range = -2 ** 31
        max_range = (2 ** 31) - 1

        res = ''
        for char in s:
            if char == ' ' and len(res) == 0:
                pass
            elif (char == '-' or char == '+') and len(res) == 0:
                res += char
            else:
                try:
                    res += str(int(char))
                except Exception:
                    break
        if res:
            try:
                res = int(res)
                if res < min_range:
                        return min_range
                elif res > max_range:
                    return max_range
                return res
            except Exception:
                pass
        return 0

sol = Solution()
print(sol.myAtoi2('+3313 14fvgfdf'))

# https://leetcode.com/problems/valid-parentheses/
class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        paren_map = {")":"(", "}":"{", "]":"["}
        char_stack = []

        for char in s:
            if char in paren_map:
                if len(char_stack) == 0 or char_stack.pop() != paren_map[char]:
                    return False
            else:
                char_stack.append(char)
        return len(char_stack) == 0


sol = Solution()
print(sol.isValid("{[][({})]}"))
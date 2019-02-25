"""
https://leetcode.com/problems/implement-strstr/
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack.

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2
Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1
"""

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        if not needle:
            return 0

        for hay_index, char in enumerate(haystack):
            if hay_index + len(needle) > len(haystack):
                return -1
            if char == needle[0]:
                needle_index = 1
                temp_hay_index = hay_index + 1
                while needle_index < len(needle):
                    if haystack[temp_hay_index] != needle[needle_index]:
                        break
                    temp_hay_index += 1
                    needle_index += 1
                if needle_index == len(needle):
                    return hay_index
        return -1

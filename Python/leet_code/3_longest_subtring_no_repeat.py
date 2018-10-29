# https://leetcode.com/problems/longest-substring-without-repeating-characters/
class Solution:
    def slowlengthOfLongestSubstring(self, s):
        """
        O(N^3)
        :type s: str
        :rtype: int
        """
        max_seen = 0
        if len(s) == 1: return 1
        for i, val_i in enumerate(s):
            seen = [val_i]
            for j, val_j in enumerate(s[i+1:]):
                if val_j in seen:
                    break
                seen.append(val_j)
            if len(seen) > max_seen:
                    max_seen = len(seen)

        return max_seen

    def fasterlengthOfLongestSubstring(self, s):
        """
        O(N^2) Using a hash table
        :type s: str
        :rtype: int
        """
        max_seen = 0
        if len(s) == 1: return 1
        for i, val_i in enumerate(s):
            seen = {}
            seen[val_i] = True
            for j, val_j in enumerate(s[i+1:]):
                if val_j in seen:
                    break
                seen[val_j] = True
            if len(seen) > max_seen:
                    max_seen = len(seen)

        return max_seen

    def lengthOfLongestSubstring(self, s):
        """
        O(N)
        :type s: str
        :rtype: int
        """
        max_num, num, sub_string = 0,0,''
        for char in s:
            if char in sub_string:
                sub_string = sub_string.split(char)[-1]+char
                num = len(sub_string)
            else:
                num += 1
                sub_string += char
                if num > max_num:
                    max_num = num
        return max_num

sol = Solution()
print(sol.lengthOfLongestSubstring("cabjhbdjvhfbu ybuvwybu"))
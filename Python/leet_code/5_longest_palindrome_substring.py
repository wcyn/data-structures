class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        def is_palindrome(self, s):
            start, end = 0, len(s) - 1
            while start <= end:
                if s[start] != s[end]:
                    return False
                start += 1
                end -= 1
            return True

        def map_char_indexes(s):
            char_map = {}
            s_len = len(s)
            for index, char in enumerate(s[::-1]):
                if char_map.get(char):
                    char_map[char].append(s_len - 1 - index)
                else:
                    char_map[char] = [s_len - 1 -index]
            return char_map

        def get_longest_palindrome_slow(s, char_map):
            max_palindrome = ''
            for i, char in enumerate(s):
                indexes = char_map[char]
                for index in indexes:
                    if is_palindrome(s[i: index + 1]):
                        # print("i: {}, index+1: {}".format(i, index+1))
                        # print(s[i: index + 1])
                        if len(s[i: index + 1]) > len(max_palindrome):
                            max_palindrome = (s[i: index + 1])
                        break
            return max_palindrome

        def get_longest_palindrome_slow(s, char_map):
            max_palindrome = ''
            for i, char in enumerate(s):
                indexes = char_map[char]
                for index in indexes:
                    if is_palindrome(s[i: index + 1]):
                        # print("i: {}, index+1: {}".format(i, index+1))
                        # print(s[i: index + 1])
                        if len(s[i: index + 1]) > len(max_palindrome):
                            max_palindrome = (s[i: index + 1])
                        break
            return max_palindrome

        def get_longest_palindrome(s):
            if len(s) < 1:
                return ''
            max_bound = (0, 0)
            for index, char in enumerate(s):
                len_bound = max_bound[1] - max_bound[0]
                bound_1 = expand_from_centre(s, index, index) # expand from single character
                bound_2 = expand_from_centre(s, index, index + 1) # expand from between two characters

                # print(bound_1, bound_2)
                if bound_1[1] - bound_1[0] > bound_2[1] - bound_2[0]:
                    potential_max_bound = bound_1
                else:
                    potential_max_bound = bound_2
                if (potential_max_bound[1] - potential_max_bound[0]) > len_bound:
                    max_bound = potential_max_bound
            print("Max:", max_bound)
            return s[max_bound[0]: max_bound[1]+1]

        def expand_from_centre(s, left, right):
            s_len = len(s)
            while left >= 0 and right < s_len and s[left] == s[right]:
                left -= 1
                right += 1

            return left+1, right-1

        # char_map = map_char_indexes(s)
        return get_longest_palindrome(s)

sol = Solution()
print(sol.longestPalindrome('ascdfggfdcknldnkna'))
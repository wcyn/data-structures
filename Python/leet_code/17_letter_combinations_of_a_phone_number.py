# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        num_char_map = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }

        if not digits or digits[0] not in num_char_map:
            return []

        # Use a list of characters instead of a string in order to save on space since
        # strings are immutable, but lists are. Avoid creating new strings every time
        char_combinations = [[char] for char in num_char_map[digits[0]]]

        # Use indexing instead of slicing to avoid creating a new string
        for index in range(1, len(digits)):
            if digits[index] not in num_char_map:
                return []
            temp_char_set = []
            for char_set in char_combinations:
                for char in num_char_map[digits[index]]:
                    temp_char_set.append(char_set + [char])
            char_combinations = list(temp_char_set)

        # Now you can combine the list of characters into strings
        return ["".join(chars) for chars in char_combinations]


"""
Details 
Runtime: 20 ms, faster than 100.00% of Python online submissions for Letter Combinations of a Phone Number.
Memory Usage: 10.7 MB, less than 81.54% of Python online submissions for Letter Combinations of a Phone Number.
"""

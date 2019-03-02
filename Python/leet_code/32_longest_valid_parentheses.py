"""
https://leetcode.com/problems/longest-valid-parentheses/
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
"""


class Solution(object):
    def longestValidParentheses1(self, s):
        """
        :type s: str
        :rtype: int
        """
        paren_counts = {
            "(": 0,
            ")": 0
        }
        max_paren_count_forward = max_paren_count_backward = 0

        for char_index in range(0, len(s)):
            paren_counts[s[char_index]] += 1
            # print "Counts 1: ", paren_counts
            if paren_counts[")"] == paren_counts["("]:
                max_paren_count_forward = max(
                    max_paren_count_forward,
                    paren_counts["("] + paren_counts[")"]
                )
                # Reset counts
            elif paren_counts[")"] > paren_counts["("]:
                paren_counts[")"] = paren_counts["("] = 0

        paren_counts = {
            "(": 0,
            ")": 0
        }

        for char_index in range(len(s) - 1, -1, -1):
            paren_counts[s[char_index]] += 1
            # print "Counts: ", paren_counts
            if paren_counts["("] == paren_counts[")"]:
                # Reset counts
                max_paren_count_backward = max(
                    max_paren_count_backward,
                    paren_counts[")"] + paren_counts["("]
                )
            elif paren_counts["("] > paren_counts[")"]:
                paren_counts[")"] = paren_counts["("] = 0

        return max(
            max_paren_count_backward,
            max_paren_count_forward
        )

    def longestValidParenthesesDepthFirst(self, s):
        """
        :type s: str
        :rtype: int
        """
        # print s
        if len(s) < 2:
            return 0

        def is_valid_parentheses(s):

            paren_stack = []
            for char in s:
                if char == "(":
                    paren_stack.append(char)
                else:
                    if not paren_stack:
                        return False
                    paren_stack.pop()
            return not paren_stack

        if is_valid_parentheses(s):
            return len(s)
        else:
            return max(
                self.longestValidParentheses(s[1:]),
                self.longestValidParentheses(s[:len(s) - 1])
            )

    def longestValidParentheses2(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import deque
        # print s
        if len(s) < 2:
            return 0

        def is_valid_parentheses(s):
            paren_stack = []
            for char in s:
                if char == "(":
                    paren_stack.append(char)
                else:
                    if not paren_stack:
                        return False
                    paren_stack.pop()
            return not paren_stack

        parens_queue = deque([s])
        while len(s) > 1:
            # print parens_queue
            s = parens_queue.pop()

            if is_valid_parentheses(s):
                return len(s)
            parens_without_start = s[1:]
            parens_without_end = s[:len(s) - 1]
            parens_queue.appendleft(parens_without_start)
            parens_queue.appendleft(parens_without_end)
        return 0

    def longestValidParentheses4(self, s):
        """
        :type s: str
        :rtype: int
        """
        paren_counts_forward = {"(": 0, ")": 0}
        paren_counts_backward = paren_counts_forward.copy()
        max_paren_count_forward = max_paren_count_backward = 0

        for char_index_forward, char_index_backward in zip(range(0, len(s)), range(len(s) - 1, -1, -1)):
            paren_counts_forward[s[char_index_forward]] += 1
            paren_counts_backward[s[char_index_backward]] += 1

            if paren_counts_forward[")"] == paren_counts_forward["("]:
                max_paren_count_forward = max(
                    max_paren_count_forward,
                    paren_counts_forward["("] + paren_counts_forward[")"]
                )
            elif paren_counts_forward[")"] > paren_counts_forward["("]:
                paren_counts_forward[")"] = paren_counts_forward["("] = 0

            if paren_counts_backward[")"] == paren_counts_backward["("]:
                max_paren_count_backward = max(
                    max_paren_count_backward,
                    paren_counts_backward["("] + paren_counts_backward[")"]
                )
            elif paren_counts_backward["("] > paren_counts_backward[")"]:
                paren_counts_backward[")"] = paren_counts_backward["("] = 0

        return max(
            max_paren_count_backward,
            max_paren_count_forward
        )

    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        stack = [0]
        longest = 0

        for c in s:
            if c == "(":
                stack.append(0)
            else:
                if len(stack) > 1:
                    val = stack.pop()
                    stack[-1] += val + 2
                    longest = max(longest, stack[-1])
                else:
                    stack = [0]

        return longest


"""
https://leetcode.com/problems/divide-two-integers/
Given two integers dividend and divisor, divide two integers without using multiplication,
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3
Example 2:

Input: dividend = 7, divisor = -3
Output: -2
Note:

- Both dividend and divisor will be 32-bit signed integers.
- The divisor will never be 0.
- Assume we are dealing with an environment which could only store integers
within the 32-bit signed integer range: [-2^31, 2^31 - 1]
- For the purpose of this problem, assume that your function
returns 2^31 - 1 when the division result overflows.
"""


class Solution(object):
    def divide_slow(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # print dividend
        MAX_INT, MIN_INT = (2 ** 31) - 1, -2 ** 31
        negative_divisor = divisor < 0
        negative_dividend = dividend < 0
        print MAX_INT
        print MIN_INT

        if not (MIN_INT <= dividend <= MAX_INT) or not (MIN_INT <= divisor <= MAX_INT):
            return MAX_INT

        dividend = abs(dividend)
        divisor = abs(divisor)

        if dividend < divisor:
            return 0

        if divisor == 1:
            if negative_divisor ^ negative_dividend:
                return -1 * dividend
            if dividend > MAX_INT:
                return MAX_INT
            return dividend

        div_count = 0
        while dividend >= 0:
            dividend -= divisor
            # print dividend
            div_count += 1

        if negative_divisor ^ negative_dividend:
            return -1 * (div_count - 1)

        return div_count - 1

    def divide_2(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

    def divide(self, dividend, divisor):
        negative = (divisor < 0) ^ (dividend < 0)
        MAX_INT, MIN_INT = (2 ** 31) - 1, -2 ** 31
        if not (MIN_INT <= dividend <= MAX_INT) or not (MIN_INT <= divisor <= MAX_INT):
            return MAX_INT

        dividend, divisor = abs(dividend), abs(divisor)

        result = 0
        while dividend >= divisor:
            temp_divisor, divisor_factor = divisor, 1
            while dividend >= temp_divisor:
                dividend -= temp_divisor
                result += divisor_factor
                temp_divisor <<= 1
                divisor_factor <<= 1

        if negative:
            return -result
        return min(MAX_INT, result)





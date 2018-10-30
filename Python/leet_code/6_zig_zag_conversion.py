class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        def zig_zag(s, numRows):
            if numRows == 1:
                return s
            column_length = numRows + (numRows - 2)
            first = mids = last = ''
            for i in range(numRows):
                if i == 0:
                    for j in range(i, len(s), column_length):
                        first += s[j]
                elif i == numRows - 1:
                    for j in range(i, len(s), column_length):
                        last += s[j]
                else:
                    for j in range(i, len(s), column_length):
                        mids += s[j]
                        next_mid = (j + column_length) - 2 * (i % column_length)
                        if next_mid < len(s):
                            mids += s[next_mid]
            return first + mids + last

        def zig_zag_faster(s, numRows):
            if numRows == 1 or numRows > len(s):
                return s
            L = [''] * numRows
            index, step = 0, 1
            for char in s:
                L[index] += char
                if index == 0:
                    step = 1
                elif index == numRows - 1:
                    step = -1
                index += step
            return ''.join(L)

        return zig_zag_faster(s, numRows)

sol = Solution()
s = "PAYPALISHIRING"
numRows = 4
print(sol.convert(s, numRows))

def test_zig_zag_with_more_than_one_row():
    sol = Solution()
    s = "PAYPALISHIRING"
    assert sol.convert(s, 4) == "PINALSIGYAHRPI"
    assert sol.convert(s, 3) == "PAHNAPLSIIGYIR"
    assert sol.convert(s, 2) == "PYAIHRNAPLSIIG"

def test_zig_zag_with_one_row():
    sol = Solution()
    s = "PAYPALISHIRING"
    assert sol.convert(s, 1) == s





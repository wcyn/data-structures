"""
Determine if a 9x9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the 9 3x3 sub-boxes of the grid must contain the digits 1-9 without repetition.

A partially filled sudoku which is valid.

The Sudoku board could be partially filled, where empty cells are filled with the character '.'.

Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.
The given board contain only digits 1-9 and the character '.'.
The given board size is always 9x9.

"""

class Solution(object):
    def isValidSudoku2(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """

        three_sets = {0: set(), 1: set(), 2: set()}
        row_sets = [None] * 9

        for row_index, row in enumerate(board):
            num_set = set([])
            for num_index, num in enumerate(row):
                if row_index % 3 == 0 and num_index == 0:
                    # print row_index, num_index
                    # Reset the numbers for the next three rows
                    # This stores numbers for the 3 by 3 boxes
                    three_sets = {0: set(), 1: set(), 2: set()}

                if num == ".":
                    continue
                num = int(num)
                # Check if duplicate number in row
                if num in num_set:
                    return False
                num_set.add(num)

                # Check if duplicate number in column
                if row_sets[num - 1]:
                    if num_index in row_sets[num - 1]:
                        return False
                    else:
                        row_sets[num - 1].add(num_index)
                else:
                    row_sets[num - 1] = set([num_index])
                row_sets[num - 1].add(num_index)

                # Check if duplicate number in square box
                # First box in three rows
                if 0 <= num_index <= 2:
                    if num in three_sets[0]:
                        return False
                    three_sets[0].add(num)

                # Second box in three rows
                elif 3 <= num_index <= 5:
                    if num in three_sets[1]:
                        return False
                    three_sets[1].add(num)

                # Third box in three rows
                elif 6 <= num_index <= 8:
                    if num in three_sets[2]:
                        return False
                    three_sets[2].add(num)
                # print three_sets, num_index

        # print three_sets
        # print row_sets
        return True

    def isValidSudoku(self, board):
        if not board:
            return False

        row, col, box = [[False] * 9 for i in range(10)], [[False] * 9 for i in range(10)], [[False] * 9 for i in
                                                                                             range(10)]

        for i in range(len(board)):
            for j in range(len(board[0])):
                num = board[i][j]
                if num != '.':
                    index = int(num) - 1
                    k = i / 3 * 3 + j / 3
                    if row[i][index] or col[j][index] or box[k][index]:
                        return False

                    row[i][index] = col[j][index] = box[k][index] = True

        return True

"""
https://leetcode.com/problems/valid-sudoku/
"""
from typing import List


def is_valid_sudoku(board: List[List[str]]) -> bool:
    box = [[set() for _ in range(3)] for _ in range(3)]
    for i in range(9):
        row = set()
        column = set()
        for j in range(9):
            r = board[i][j]
            c = board[j][i]
            if r != '.':
                if r in row or r in box[i // 3][j // 3]:
                    return False
                box[i // 3][j // 3].add(r)
                row.add(r)
            if c != '.':
                if c in column:
                    return False
                column.add(c)
    return True


if __name__ == '__main__':
    b = [["5", "3", ".", ".", "7", ".", ".", ".", "."]
        , ["6", ".", ".", "1", "9", "5", ".", ".", "."]
        , [".", "9", "8", ".", ".", ".", ".", "6", "."]
        , ["8", ".", ".", ".", "6", ".", ".", ".", "3"]
        , ["4", ".", ".", "8", ".", "3", ".", ".", "1"]
        , ["7", ".", ".", ".", "2", ".", ".", ".", "6"]
        , [".", "6", ".", ".", ".", ".", "2", "8", "."]
        , [".", ".", ".", "4", "1", "9", ".", ".", "5"]
        , [".", ".", ".", ".", "8", ".", ".", "7", "9"]]
    print(is_valid_sudoku(b))

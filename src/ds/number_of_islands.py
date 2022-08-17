"""
https://leetcode.com/problems/number-of-islands/
"""
from typing import List


def number_of_islands(grid: List[List[str]]) -> int:
    counter = 2

    def fill_island(grid, i, j, counter):
        if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[i]):
            return
        if grid[i][j] != "1":
            return
        grid[i][j] = counter
        fill_island(grid, i - 1, j, counter)
        fill_island(grid, i, j - 1, counter)
        fill_island(grid, i + 1, j, counter)
        fill_island(grid, i, j + 1, counter)

    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == "1":
                fill_island(grid, i, j, str(counter))
                counter += 1
    return counter - 2


if __name__ == '__main__':
    print(number_of_islands([
        ["1", "1", "1", "1", "0"],
        ["1", "1", "0", "1", "0"],
        ["1", "1", "0", "0", "0"],
        ["0", "0", "0", "0", "0"]
    ]))

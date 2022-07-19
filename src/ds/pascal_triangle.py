"""
https://leetcode.com/problems/pascals-triangle/
"""
from typing import List


def pascal_triangle(n: int) -> List[List[int]]:
    store = [[1] * i for i in range(1, n + 1)]
    for i in range(2, n):
        for j in range(1, i):
            store[i][j] = store[i - 1][j] + store[i - 1][j - 1]
    return store


if __name__ == '__main__':
    print(pascal_triangle(5))

"""
https://leetcode.com/problems/unique-paths/
"""


def unique_paths(m: int, n: int) -> int:
    store = [[-1 for i in range(n)] for j in range(m)]
    store[-1][-1] = 0
    for i in range(m):
        store[i][-1] = 1
    for i in range(n):
        store[-1][i] = 1
    for i in range(m - 2, -1, -1):
        for j in range(n - 2, -1, -1):
            store[i][j] = store[i + 1][j] + store[i][j + 1]
    return store[0][0]


if __name__ == '__main__':
    print(unique_paths(3, 2))

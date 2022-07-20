"""
https://leetcode.com/problems/climbing-stairs/
"""


def climb_stairs(n: int) -> int:
    store = [1 for _ in range(n + 1)]
    for i in range(2, n + 1):
        store[i] = store[i - 1]
        if i - 2 >= 0:
            store[i] += store[i - 2]
    return store[-1]


if __name__ == '__main__':
    print(climb_stairs(10))

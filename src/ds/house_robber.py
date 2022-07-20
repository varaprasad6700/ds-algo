"""
https://leetcode.com/problems/house-robber/
"""
from typing import List


def rob(nums: List[int]) -> int:
    store = [i for i in nums]
    for i in range(1, len(nums)):
        if i == 1:
            store[i] = max(store[0], store[1])
        else:
            store[i] = max(store[i - 1], store[i] + store[i - 2])
    return store[-1]


if __name__ == '__main__':
    print(rob([1, 2, 3, 1]))

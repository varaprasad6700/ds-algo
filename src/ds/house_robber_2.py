"""
https://leetcode.com/problems/house-robber-ii/
"""
from typing import List


def rob(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    else:
        store = [0, 0]
        for i in range(len(nums) - 1):
            store[0], store[1] = store[1], max(store[1], store[0] + nums[i])
        temp = store[-1]
        store = [0, 0]
        for i in range(1, len(nums)):
            store[0], store[1] = store[1], max(store[1], store[0] + nums[i])
        return max(temp, store[-1])


if __name__ == '__main__':
    print(rob([2, 3, 2]))

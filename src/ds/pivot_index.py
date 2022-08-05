"""
https://leetcode.com/problems/find-pivot-index/
"""
from typing import List


def pivot_index(nums: List[int]) -> int:
    total = sum(nums)
    ls = 0
    for i in range(len(nums)):
        if ls == total - ls - nums[i]:
            return i
        ls += nums[i]
    return -1


if __name__ == '__main__':
    print(pivot_index([1, 7, 3, 6, 5, 6]))

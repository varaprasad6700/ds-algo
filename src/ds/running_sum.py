"""
https://leetcode.com/problems/running-sum-of-1d-array/
"""
from typing import List


def running_sum(nums: List[int]) -> List[int]:
    for i in range(1, len(nums)):
        nums[i] += nums[i - 1]
    return nums


if __name__ == '__main__':
    print(running_sum([1, 2, 3, 4, 5]))

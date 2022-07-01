"""
https://leetcode.com/problems/move-zeroes/
"""
from typing import List


def move_zeros(nums: List[int]) -> List[int]:
    pos = 0
    i = 0
    while i < len(nums):
        if nums[i] != 0:
            nums[pos], nums[i] = nums[i], nums[pos]
            pos += 1
        i += 1
    return nums


if __name__ == '__main__':
    print(move_zeros([0, 1, 0, 3, 12]))

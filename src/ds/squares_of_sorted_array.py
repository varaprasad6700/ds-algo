"""
https://leetcode.com/problems/squares-of-a-sorted-array/
"""
from typing import List


def squares_of_sorted_array(nums: List[int]) -> List[int]:
    l = 0
    r = len(nums) - 1
    pos = r
    out = [0 for _ in nums]
    while l <= r:
        if abs(nums[l]) > abs(nums[r]):
            out[pos] = nums[l] ** 2
            pos -= 1
            l += 1
        else:
            out[pos] = nums[r] ** 2
            pos -= 1
            r -= 1
    return out


if __name__ == '__main__':
    print(squares_of_sorted_array([-4, -1, 0, 3, 10]))

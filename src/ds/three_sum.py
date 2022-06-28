"""
https://leetcode.com/problems/3sum/
"""
from typing import List


def three_sum(nums: List[int]) -> List[List[int]]:
    nums.sort()
    n = len(nums)
    out = set()
    for i in range(n):
        l = i + 1
        r = n - 1
        while l < r:
            val = nums[i] + nums[l] + nums[r]
            if val == 0:
                out.add((nums[i], nums[l], nums[r]))
                l += 1
                r -= 1
            elif val > 0:
                r -= 1
            else:
                l += 1
    return [list(i) for i in out]


if __name__ == '__main__':
    print(three_sum([-1, 0, 1, 2, -1, -4]))

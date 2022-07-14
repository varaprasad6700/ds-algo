"""
https://leetcode.com/problems/trapping-rain-water/
"""
from typing import List


def trap_rain_water(height: List[int]) -> int:
    out = 0
    l = 0
    r = len(height) - 1
    lmax = height[l]
    rmax = height[r]
    while l < r:
        if height[l] < height[r]:
            if height[l] > lmax:
                lmax = height[l]
            else:
                out += lmax - height[l]
            l += 1
        else:
            if height[r] > rmax:
                rmax = height[r]
            else:
                out += rmax - height[r]
            r -= 1
    return out


if __name__ == '__main__':
    print(trap_rain_water([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))

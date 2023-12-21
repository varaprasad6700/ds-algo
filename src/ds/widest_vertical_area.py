"""
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points
"""
from typing import List

def max_width_of_vertical_area(points: List[List[int]]) -> int:
        temp = map(lambda x: x[0], sorted(points, key=lambda x: x[0]))
        return max(j - i for (i, j) in zip(temp[:-1], temp[1:]))
                
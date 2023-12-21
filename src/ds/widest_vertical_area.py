"""
https://leetcode.com/problems/widest-vertical-area-between-two-points-containing-no-points
"""
def max_width_of_vertical_area(points: List[List[int]]) -> int:
        temp = map(sorted(points, key=lambda x: x[0]), lambda x: x[0])
        return max(j - i for (i, j) in zip(temp[:-1], temp[1:]))
                
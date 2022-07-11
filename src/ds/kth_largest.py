"""
https://leetcode.com/problems/kth-largest-element-in-an-array/
"""

import heapq
from typing import List


def find_kth_largest(nums: List[int], k: int) -> int:
    return heapq.nlargest(k, nums)[-1]


if __name__ == '__main__':
    print(find_kth_largest([3, 2, 1, 5, 6, 4], 2))
    print(find_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))

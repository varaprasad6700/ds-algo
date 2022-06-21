"""
https://leetcode.com/problems/binary-search/
"""
from typing import List


def search(nums: List[int], target: int) -> int:
    n = len(nums)

    def b_search(nums: List[int], l: int, r: int, target: int) -> int:
        mid = (l + r) // 2
        if l > r:
            return -1
        elif nums[mid] == target:
            return mid
        elif nums[mid] > target:
            return b_search(nums, l, mid - 1, target)
        else:
            return b_search(nums, mid + 1, r, target)

    return b_search(nums, 0, n - 1, target)


if __name__ == '__main__':
    ns = [-1, 0, 3, 5, 9, 12]
    print(search(ns, 9))

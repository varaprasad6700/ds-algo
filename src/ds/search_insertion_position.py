"""
https://leetcode.com/problems/search-insert-position/
"""
from typing import List


def search_insertion_position(nums: List[int], target: int) -> int:
    left = 0
    right = len(nums) - 1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] > target:
            right = mid - 1
        else:
            left = mid + 1
    return left


if __name__ == '__main__':
    print(search_insertion_position([1, 3, 5, 6], 5))

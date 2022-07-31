"""
https://leetcode.com/problems/longest-increasing-subsequence/
"""
from typing import List


def longest_increasing_subsequence(nums: List[int]) -> int:
    store = [1 for i in nums]
    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j] and store[j] + 1 > store[i]:
                store[i] = store[j] + 1
    return max(store)


if __name__ == '__main__':
    print(longest_increasing_subsequence([10, 9, 2, 5, 3, 7, 101, 18]))

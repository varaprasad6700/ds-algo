"""
https://leetcode.com/problems/majority-element/
"""

from collections import Counter
from typing import List


def majority_element_dict(nums: List[int]) -> int:
    c = Counter(nums)
    return c.most_common(1)[0][0]


def majority_element_div_and_conquer(nums: List[int], l: int = 0, r: int = None) -> int:
    if l == r:
        return nums[l]
    mid = (r + l) // 2
    left = majority_element_div_and_conquer(nums, l, mid)
    right = majority_element_div_and_conquer(nums, mid + 1, r)
    if left == right:
        return left
    lc = 0
    rc = 0
    for i in range(l, r + 1):
        if nums[i] == left:
            lc += 1
        if nums[i] == right:
            rc += 1
    return left if lc > rc else right


def majority_element_boyer_moore_voting(nums: List[int]) -> int:
    """
    works only if an element is present more than n/2 times
    """
    candidate = -1
    votes = 0
    for i in nums:
        if votes == 0:
            candidate = i
            votes += 1
        elif i == candidate:
            votes += 1
        else:
            votes -= 1
    return candidate


if __name__ == '__main__':
    nums = [2, 2, 1, 1, 1, 2, 2]
    print(majority_element_dict(nums))
    print(majority_element_div_and_conquer(nums, 0, len(nums) - 1))
    print(majority_element_boyer_moore_voting(nums))

"""
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
from typing import List


def remove_duplicates(nums: List[int]) -> int:
    k = 1
    prev = nums[0]
    insert_pos = 1
    i = 1
    while i < len(nums):
        if nums[i] != prev:
            prev = nums[i]
            k += 1
            nums[insert_pos], nums[i] = nums[i], nums[insert_pos]
            insert_pos += 1
            i += 1
        else:
            i += 1
    return k


if __name__ == '__main__':
    inp = [0, 0, 1, 1, 1, 2, 2, 3, 3, 4]
    print(remove_duplicates(inp))
    print(inp)

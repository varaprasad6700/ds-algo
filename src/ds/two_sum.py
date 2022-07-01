"""
https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
"""
from typing import List


def two_sum(numbers: List[int], target: int) -> List[int]:
    l = 0
    r = len(numbers) - 1
    while l < r:
        temp = numbers[l] + numbers[r]
        if temp == target:
            return [l + 1, r + 1]
        elif temp > target:
            r -= 1
        else:
            l += 1


if __name__ == '__main__':
    print(two_sum([2, 7, 11, 15], 9))

"""
https://leetcode.com/problems/rotate-array/
"""
from typing import List


def rotate_array(nums: List[int], k: int) -> None:
    n = len(nums)
    k = k % n
    temp = 0
    for i in nums[-k:] + nums[:-k]:
        nums[temp] = i
        temp += 1


def rotate_array_optimized(nums: List[int], k: int) -> None:
    def reverse(arr: List[int], l: int, r: int):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    n = len(nums)
    k = k % n
    reverse(nums, 0, n - 1)
    reverse(nums, 0, k - 1)
    reverse(nums, k, n - 1)


if __name__ == '__main__':
    inp = [1, 2, 3, 4, 5, 6, 7]
    k = 3
    rotate_array_optimized(inp, k)
    print(inp)

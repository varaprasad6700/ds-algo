"""
https://leetcode.com/problems/maximum-subarray/
"""

from typing import List


def max_sub_array(nums: List[int]) -> int:
    max_sum = nums[0]
    current_sum = nums[0]
    for i in range(1, len(nums)):
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    return max_sum


def max_sub_array_with_start_and_end(nums: List[int]) -> List[int]:
    max_sum = nums[0]
    current_sum = nums[0]
    start = 0
    end = 0
    temp_start = 0
    for i in range(1, len(nums)):
        if nums[i] > current_sum + nums[i]:
            temp_start = i
            current_sum = max(nums[i], current_sum + nums[i])
        else:
            current_sum = max(nums[i], current_sum + nums[i])
        if current_sum > max_sum:
            start = temp_start
            end = i
            max_sum = max(max_sum, current_sum)
    return [max_sum, start, end]


if __name__ == '__main__':
    print(max_sub_array([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
    print(max_sub_array_with_start_and_end([5, 4, -1, 7, 8]))

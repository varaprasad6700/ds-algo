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

if __name__ == '__main__':
    print(max_sub_array([-2,1,-3,4,-1,2,1,-5,4]))
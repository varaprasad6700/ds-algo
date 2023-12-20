"""
https://leetcode.com/problems/combination-sum-iv/
"""
from typing import List


def combination_sum_4(nums: List[int], target: int) -> int:
    dp = [0 for i in range(target + 1)]
    dp[0] = 1
    for i in range(len(dp)):
        for j in nums:
            if j <= i:
                dp[i] += dp[i - j]
    return dp[-1]


if __name__ == '__main__':
    print(combination_sum_4([1, 2, 3], 4))

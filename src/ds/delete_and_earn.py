"""
https://leetcode.com/problems/delete-and-earn/
"""
from typing import List


def delete_and_earn(nums: List[int]) -> int:
    store = {}
    temp = 0
    for i in nums:
        store[i] = store.get(i, 0) + i
        temp = max(temp, i)
    dp = [0 for i in range(temp + 1)]
    dp[1] = store.get(1, 0)
    for i in range(2, len(dp)):
        dp[i] = max(dp[i - 1], dp[i - 2] + store.get(i, 0))
    return dp[temp]


if __name__ == '__main__':
    print(delete_and_earn([2, 2, 3, 3, 3, 4]))

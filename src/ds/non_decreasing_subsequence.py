"""
https://leetcode.com/problems/non-decreasing-subsequences/
"""
from typing import List


def find_subsequences(nums: List[int]) -> List[List[int]]:
    out = []
    store = []

    def dfs(i: int, prev: int) -> None:
        if i == len(nums):
            if len(store) >= 2:
                out.append(store.copy())
            return

        if len(store) == 0 or nums[i] >= prev:
            store.append(nums[i])
            dfs(i + 1, nums[i])
            store.pop()
        if i > 0 and len(store) != 0 and store[-1] == nums[i]:
            return
        dfs(i + 1, prev)

    dfs(0, -10000)
    return out


if __name__ == '__main__':
    print(find_subsequences([4, 6, 7, 7]))

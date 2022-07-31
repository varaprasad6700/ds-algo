"""
https://leetcode.com/problems/range-sum-query-mutable/
"""
from typing import List


class RangeSumQuery:

    def __init__(self, nums: List[int]):
        self.n = len(nums)
        self.tree = [0 for i in range(2 * self.n)]
        j = 0
        for i in range(self.n, 2 * self.n):
            self.tree[i] = nums[j]
            j += 1
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.tree[i * 2] + self.tree[i * 2 + 1]

    def update(self, index: int, val: int) -> None:
        index += self.n
        self.tree[index] = val
        while index > 0:
            if index % 2 == 0:
                right = index + 1
                left = index
            else:
                left = index - 1
                right = index
            self.tree[index // 2] = self.tree[left] + self.tree[right]
            index //= 2

    def sum_range(self, left: int, right: int) -> int:
        left += self.n
        right += self.n
        out = 0
        while left <= right:
            if left % 2 == 1:
                out += self.tree[left]
                left += 1
            if right % 2 == 0:
                out += self.tree[right]
                right -= 1
            left //= 2
            right //= 2
        return out


if __name__ == '__main__':
    ob = RangeSumQuery([1, 3, 5])
    print(ob.sum_range(0, 2))
    ob.update(1, 2)
    print(ob.sum_range(0, 2))

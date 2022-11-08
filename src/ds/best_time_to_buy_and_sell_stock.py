"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
"""
from typing import List


def max_profit(prices: List[int]) -> int:
    prev_least = prices[0]
    max_p = 0
    for i in prices[1:]:
        if i < prev_least:
            prev_least = i
        else:
            max_p = max(max_p, i - prev_least)
    return max_p


if __name__ == '__main__':
    print(max_profit([7, 1, 5, 3, 6, 4]))

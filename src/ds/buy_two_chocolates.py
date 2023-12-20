"""
https://leetcode.com/problems/buy-two-chocolates/
"""
import math
from typing import List


def buy_choco(prices: List[int], money: int) -> int:
    lowest = math.inf
    second_lowest = math.inf
    for i in prices:
        if i < lowest:
            lowest, second_lowest = i, lowest
        elif i < second_lowest:
            second_lowest = i
    min_price = lowest + second_lowest
    if min_price > money:
        return money
    else:
        return money - min_price


if __name__ == '__main__':
    print(buy_choco([1, 2, 2], money=3))

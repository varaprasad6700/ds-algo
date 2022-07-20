"""
https://leetcode.com/problems/min-cost-climbing-stairs/
"""
from typing import List


def min_cost_climbing_stairs(cost: List[int]) -> int:
    min_cost = [0 for _ in range(len(cost) + 1)]
    for i in range(len(cost) + 1):
        if i < 2:
            min_cost[i] = 0
        else:
            min_cost[i] = min(min_cost[i - 1] + cost[i - 1], min_cost[i - 2] + cost[i - 2])
    return min_cost[-1]


if __name__ == '__main__':
    print(min_cost_climbing_stairs([1, 100, 1, 1, 1, 100, 1, 1, 100, 1]))

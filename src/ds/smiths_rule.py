"""
The following problem arises in supply chain management.
You have a bunch of jobs to schedule on a single machine.
Job j requires p[j] units of processing time.
Job j has a positive weight w[j] which represents its relative importance -
think of it as the inventory cost of storing the raw materials for job j for 1 unit of time.
If job j finishes being processed at time t, then it costs t * w[j] dollars.
The goal is to sequence the jobs to minimize the sum of the weighted completion times of each job.
Output an optimal sequence in which to process their jobs.
Hint: Use Smith's rule: schedule the jobs in order of their ratio of processing time to weight.
"""
import math
from typing import List

from src.ds.merge_sort import merge_sort


def smiths_rule(n: int, p: List[int], w: List[int]) -> List[int]:
    order = []
    ratios = [w[i] / p[i] for i in range(n)]
    original = ratios[:]
    merge_sort(ratios, 0, n - 1)
    ratios.reverse()
    for i in range(n):
        for j in range(n):
            if math.isclose(original[j], ratios[i]):
                order.append(j)
    return order


if __name__ == '__main__':
    n = int(input())
    p = [int(i) for i in input().split()]
    w = [int(i) for i in input().split()]
    print(smiths_rule(n, p, w))

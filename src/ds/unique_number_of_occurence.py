"""
https://leetcode.com/problems/unique-number-of-occurrences/description/
"""
from collections import Counter
from typing import List


def unique_occurrence(arr: List[int]) -> bool:
    counter = Counter(arr)
    return len(counter.values()) == len(set(counter.values()))


if __name__ == '__main__':
    print(unique_occurrence([1, 2, 2, 1, 1, 3]))

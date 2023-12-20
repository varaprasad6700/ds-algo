"""
https://leetcode.com/problems/sort-characters-by-frequency/description/
"""

from collections import Counter


def frequency_sort(s: str) -> str:
    return "".join([i[0] * i[1] for i in sorted(Counter(s).items(), key=lambda x: -x[1])])

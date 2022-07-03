"""
https://leetcode.com/problems/permutation-in-string/
"""
from collections import Counter


def check_inclusion(s1: str, s2: str) -> bool:
    if len(s1) > len(s2):
        return False
    c = Counter(s1)
    l = 0
    r = 0
    d = {}
    for i in range(len(s1)):
        d[s2[i]] = d.get(s2[i], 0) + 1
        r += 1
    while l < len(s2) - len(s1):
        if c == d:
            return True
        d[s2[r]] = d.get(s2[r], 0) + 1
        d[s2[l]] -= 1
        if d[s2[l]] == 0:
            del d[s2[l]]
        r += 1
        l += 1
    return c == d


if __name__ == '__main__':
    s1 = "ab"
    s2 = "eidbaooo"
    print(check_inclusion(s1, s2))
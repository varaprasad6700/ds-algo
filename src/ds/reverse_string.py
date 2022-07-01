"""
https://leetcode.com/problems/reverse-string/
"""
from typing import List


def reverse_string(s: List[str]) -> None:
    l = 0
    r = len(s) - 1
    while l < r:
        s[l], s[r] = s[r], s[l]
        l += 1
        r -= 1


if __name__ == '__main__':
    s = ["h", "e", "l", "l", "o"]
    reverse_string(s)
    print(s)
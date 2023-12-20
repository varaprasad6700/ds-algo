"""
https://leetcode.com/problems/first-unique-character-in-a-string/
"""
from collections import Counter


def first_unique_char(s: str) -> int:
    store = Counter(s)
    for i in range(len(s)):
        if store[s[i]] == 1:
            return i
    return -1


if __name__ == '__main__':
    print(first_unique_char("leetcode"))

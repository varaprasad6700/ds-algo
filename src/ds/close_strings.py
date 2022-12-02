"""
https://leetcode.com/problems/determine-if-two-strings-are-close/description/
"""
from collections import Counter


def close_strings(word1: str, word2: str) -> bool:
    w1 = Counter(word1)
    w2 = Counter(word2)
    return w1.keys() == w2.keys() and sorted(w1.values()) == sorted(w2.values())


if __name__ == '__main__':
    print(close_strings("abc", "bca"))

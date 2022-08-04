"""
Given two strings s and t, determine if they are isomorphic. Two strings s and t are isomorphic if the characters
in s can be replaced to get t. All occurrences of a character must be replaced with another character while
preserving the order of characters. No two characters may map to the same character, but a character may map to itself.

Example 1:
Input: s = "egg", t = "add"
Output: true

Example 2:
Input: s = "foo", t = "bar"
Output: false

Example 3:
Input: s = "paper", t = "title"
Output: true
"""
import string
from typing import Optional, List


def check_isomorphic(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
    if len(s) == 1:
        return True
    letters = string.ascii_lowercase
    map_arr: List[Optional[int]] = [None for _ in letters]
    used = [0 for _ in letters]
    for i in range(len(s)):
        ind1 = ord(s[i]) - ord('a')
        ind2 = ord(t[i]) - ord('a')
        if map_arr[ind1] is None:
            if used[ind2] != 0:
                return False
            map_arr[ind1] = ind2
            used[ind2] = 1
        elif map_arr[ind1] != ind2:
            return False
    return True


if __name__ == '__main__':
    print(check_isomorphic('egg', 'add'))
    print(check_isomorphic('foo', 'bar'))
    print(check_isomorphic('paper', 'title'))
    print(check_isomorphic('egs', 'add'))

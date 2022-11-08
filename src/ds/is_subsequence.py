"""
https://leetcode.com/problems/is-subsequence/
"""


def is_subsequence(s: str, t: str) -> bool:
    if len(s) == 0:
        return True
    temp = 0
    for i in t:
        if i == s[temp]:
            temp += 1
            if temp == len(s):
                return True
    return False


if __name__ == '__main__':
    print(is_subsequence("abc", "ahbgdc"))

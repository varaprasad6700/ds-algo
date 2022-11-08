"""
https://leetcode.com/problems/longest-palindrome/
"""
from collections import Counter


def longest_palindrome(s: str) -> int:
    dp = Counter(s)
    out_ = 0
    for i in dp:
        out_ += (dp[i] // 2) * 2
        if out_ % 2 == 0 and dp[i] % 2 == 1:
            out_ += 1
    return out_


if __name__ == '__main__':
    print(longest_palindrome("abccccdd"))

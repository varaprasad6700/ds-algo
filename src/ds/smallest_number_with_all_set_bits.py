"""
https://leetcode.com/problems/smallest-number-with-all-set-bits
"""


def smallest_number(n: int) -> int:
    out = 1
    while out < n:
        out = out * 2 + 1
    return out


if __name__ == '__main__':
    print(smallest_number(10))
"""
https://leetcode.com/problems/string-to-integer-atoi/
"""


def string_to_integer(s: str) -> int:
    out = 0
    ind = 0
    while ind < len(s) and s[ind] == ' ':
        ind += 1
    sign = 1
    if ind >= len(s):
        return out
    if s[ind] == '-':
        ind += 1
        sign = -1
    elif s[ind] == '+':
        ind += 1
    temp = ""
    while ind < len(s) and s[ind].isdigit():
        temp += s[ind]
        ind += 1
    temp_ind = 0
    INT_MAX = (2 ** 31) - 1
    INT_MIN = -(2 ** 31)
    while temp_ind < len(temp):
        curr = int(temp[temp_ind])
        if out > INT_MAX // 10 or (out == INT_MAX // 10 and curr > INT_MAX % 10):
            return INT_MAX if sign == 1 else INT_MIN
        out = out * 10 + curr
        temp_ind += 1
    return out if sign == 1 else (-1) * out


if __name__ == '__main__':
    print(string_to_integer("       -42"))

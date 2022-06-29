"""
https://leetcode.com/problems/roman-to-integer/
"""


def roman_to_int(s: str) -> int:
    order = ['I', 'V', 'X', 'L', 'C', 'D', 'M']
    vals = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
    out_ = 0
    ind = 0
    while ind < len(s):
        curr = s[ind]
        if ind >= len(s) - 1:
            out_ += vals[curr]
        else:
            nex = s[ind + 1]
            if order.index(nex) > order.index(curr):
                out_ -= vals[curr]
            else:
                out_ += vals[curr]
        ind += 1
    return out_


if __name__ == '__main__':
    print(roman_to_int("MCMXCIV"))

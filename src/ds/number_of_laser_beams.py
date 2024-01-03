"""
https://leetcode.com/problems/number-of-laser-beams-in-a-bank/
"""
from typing import List


def number_of_beams(bank: List[int]) -> int:
    prev = None
    curr = None
    out = 0
    for i in bank:
        current_sum = i.count('1')
        if current_sum != 0:
            curr, prev = current_sum, curr
            if curr is not None and prev is not None:
                out += curr * prev
    return out


if __name__ == '__main__':
    print(max_profit(["011001", "000000", "010100", "001000"]))

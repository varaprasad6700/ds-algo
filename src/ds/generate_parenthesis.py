"""
https://leetcode.com/problems/generate-parentheses/
"""
from typing import List


def generate_parenthesis(n: int) -> List[str]:
    if n == 0:
        return [""]
    out = []
    for i in range(n):
        for l in generate_parenthesis(i):
            for r in generate_parenthesis(n - 1 - i):
                out.append("({}){}".format(l, r))
    return out


if __name__ == '__main__':
    print(generate_parenthesis(3))

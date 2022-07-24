"""
https://leetcode.com/problems/longest-valid-parentheses/
"""


def longest_valid_parenthesis(s: str) -> int:
    stack = [-1]
    out = 0
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        else:
            stack.pop()
            if len(stack) == 0:
                stack.append(i)
            else:
                out = max(out, i - stack[-1])
    return out


if __name__ == '__main__':
    print(longest_valid_parenthesis(")()())"))

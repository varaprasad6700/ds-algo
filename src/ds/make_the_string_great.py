"""
https://leetcode.com/problems/make-the-string-great/
"""


def make_good(s: str) -> str:
    if len(s) <= 1:
        return s
    else:
        right = make_good(s[1:])
        if len(right) != 0 and compare(s[0], right[0]):
            return right[1:]
        return s[0] + right


def compare(left: str, right: str) -> bool:
    return (left.isupper() ^ right.isupper()) and (left.casefold() == right.casefold())


if __name__ == '__main__':
    print(make_good("abBAcC"))
    print(make_good("leEeetcode"))

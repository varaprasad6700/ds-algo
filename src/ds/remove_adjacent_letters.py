"""
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


def remove_duplicates(s: str) -> str:
    lis = []
    for i in s:
        if lis and lis[-1] == i:
            lis.pop()
        else:
            lis.append(i)
    return "".join(lis)


if __name__ == '__main__':
    print(remove_duplicates("abbaca"))

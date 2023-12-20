"""
https://leetcode.com/problems/determine-if-string-halves-are-alike/
"""


def halves_are_alike(s: str) -> bool:
    left_count = 0
    right_count = 0
    mid = len(s) // 2
    vowels = 'aeiouAEIOU'
    for i in range(mid):
        if s[i] in vowels:
            left_count += 1
        if s[mid + i] in vowels:
            right_count += 1
    return left_count == right_count


if __name__ == '__main__':
    print(halves_are_alike("book"))

"""
https://leetcode.com/problems/reverse-words-in-a-string-iii/
"""


def reverse_words(s: str) -> str:
    s = list(s)
    l = 0

    def reverse(s, l, r):
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1

    while l < len(s):
        r = l
        while r < len(s) and s[r] != ' ':
            r += 1
        reverse(s, l, r - 1)
        l = r + 1
    return "".join(s)


if __name__ == '__main__':
    s = "Let's take LeetCode contest"
    print(reverse_words(s))

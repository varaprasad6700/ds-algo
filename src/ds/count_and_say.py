"""
https://leetcode.com/problems/count-and-say/
"""


def count_and_say(n: int) -> str:
    out = ["1"]
    n -= 1
    while n > 0:
        temp = []
        curr = out[0]
        i = 0
        while i < len(curr):
            count = 0
            p = curr[i]
            count += 1
            j = i + 1
            while j < len(curr) and curr[j] == p:
                j += 1
                count += 1
            i = j
            temp += [str(count), p]
        out = ["".join(temp)]
        n -= 1
    return out[0]


if __name__ == '__main__':
    print(count_and_say(1))
    print(count_and_say(4))

"""
https://projecteuler.net/problem=36
"""


def get_palindrome(n: int, odd: bool) -> int:
    if odd:
        return int(str(n) + str(n)[-2::-1])
    else:
        return int(str(n) + str(n)[::-1])


def is_palindrome(n: str):
    n = n[2:]  # binary numbers start with 0b
    return n == n[::-1]


def double_base_palindrome_sum(m: int) -> int:
    out_ = 0
    i = 1
    temp = get_palindrome(i, True)
    while temp < m:
        if is_palindrome(bin(temp)):
            out_ += temp
        i += 1
        temp = get_palindrome(i, True)
    i = 1
    temp = get_palindrome(i, False)
    while temp < m:
        if is_palindrome(bin(temp)):
            out_ += temp
        i += 1
        temp = get_palindrome(i, False)
    return out_


if __name__ == '__main__':
    m = 1_000_000
    print(double_base_palindrome_sum(m))

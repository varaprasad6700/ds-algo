"""
https://projecteuler.net/problem=9
"""
from typing import List


def pythagorean_triplet(n: int) -> List[int]:
    temp = n ** 2
    for a in range(1, n // 3):
        for b in range(a + 1, (n - a) // 2):
            if temp == 2 * (n * (a + b) - (a * b)):
                return [a, b, n - (a + b)]


if __name__ == '__main__':
    print(pythagorean_triplet(1000))

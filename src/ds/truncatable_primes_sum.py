from typing import List, Set

primes: Set[int] = {2, 3, 5, 7}


def left_truncatable(n: int) -> bool:
    for i in range(1, len(str(n))):
        if int(str(n)[i:]) not in primes:
            return False
    return True


def right_truncatable(n: int) -> bool:
    for i in range(1, len(str(n))):
        if int(str(n)[:i]) not in primes:
            return False
    return True


def is_prime(n: int) -> bool:
    if n in primes:
        return True
    if n % 2 == 0:
        return False
    for i in range(3, int(n ** 0.5) + 1, 2):
        if n % i == 0:
            return False
    return True


def truncatable_prime_sum(n: int) -> int:
    i = 9
    out_: List[int] = []
    while 11 >= n > len(out_):
        if is_prime(i):
            primes.add(i)
            if left_truncatable(i) and right_truncatable(i):
                out_.append(i)
                # print(out_)
        i += 2
    return sum(out_)


if __name__ == '__main__':
    print(truncatable_prime_sum(11))

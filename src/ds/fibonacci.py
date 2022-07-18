"""
https://leetcode.com/problems/fibonacci-number/
"""


def fib(n: int) -> int:
    arr = [0, 1]
    if n < 2:
        return arr[n]
    else:
        n -= 2
        while n >= 0:
            arr[0], arr[1] = arr[1], arr[0] + arr[1]
            n -= 1
        return arr[-1]


store = {0: 0, 1: 1}


def fib_td(n: int) -> int:
    if n in store:
        return store[n]
    else:
        store[n] = fib(n - 1) + fib(n - 2)
        return store[n]


if __name__ == '__main__':
    print(fib(10))
    print(fib_td(10))

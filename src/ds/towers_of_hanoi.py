"""
towers of hanoi recursive
"""


def towers_of_hanoi(n: int, t1: str, t2: str, t3: str) -> None:
    if n == 0:
        return
    else:
        towers_of_hanoi(n - 1, t1, t3, t2)
        print("move {} from {} to {}".format(n, t1, t2))
        towers_of_hanoi(n - 1, t3, t2, t1)


if __name__ == '__main__':
    towers_of_hanoi(4, 'a', 'c', 'b')

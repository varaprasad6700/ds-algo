"""
https://leetcode.com/problems/n-th-tribonacci-number/
"""


def tribonacci(n: int) -> int:
    arr = [0, 1, 1]
    if n < 2:
        return arr[n]
    elif n == 2:
        return 1
    else:
        n -= 3
        while n > 0:
            arr[0], arr[1], arr[2] = arr[1], arr[2], arr[1] + arr[2] + arr[0]
            n -= 1
        return sum(arr)


if __name__ == '__main__':
    print(tribonacci(25))

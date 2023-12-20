"""
https://leetcode.com/problems/power-of-four/
"""


# better condition n != 0 and n &(n-1) == 0 and n & 1431655765== n
# slower solution
def is_power_of_four(n: int) -> bool:
    while True:
        if n == 1:
            return True
        elif n < 1 or n & 3 != 0:
            return False
        n = n >> 2


if __name__ == '__main__':
    print(is_power_of_four(1024))

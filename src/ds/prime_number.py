from math import sqrt


def is_prime(num: int) -> bool:
    if num == 2:
        return True
    elif num % 2 == 0:
        return False
    else:
        for j in range(3, int(sqrt(num)) + 1):
            if num % j == 0:
                return False
        else:
            return True


if __name__ == '__main__':
    print(is_prime(2))
    print(is_prime(3))
    print(is_prime(4))
    print(is_prime(1000))

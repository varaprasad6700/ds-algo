"""

"""
from typing import List


def max_area(height: List[int]) -> int:
    left = 0
    right = len(height) - 1
    max_val = 0
    while left < right:
        val = water(height, left, right)
        if val > max_val:
            max_val = val
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
        else:
            if height[left] > height[right]:
                right -= 1
            else:
                left += 1
    return max_val


def water(height: List[int], left: int, right: int) -> int:
    return (right - left) * min(height[left], height[right])


if __name__ == '__main__':
    print(max_area([1, 8, 6, 2, 5, 4, 8, 3, 7]))

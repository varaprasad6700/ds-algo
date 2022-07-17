import math
from typing import Optional


def linear_search(nums: [int], target: int) -> int:
    i = 0
    while i < len(nums):
        if nums[i] == target:
            return i
        i += 1
    else:
        return -1


def binary_search_sorted(nums: [int], target: int) -> int:
    l = 0
    r = len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            l = mid + 1
        else:
            r = mid - 1
    else:
        return -1


def binary_search_unsorted(nums: [int], target: int) -> int:
    temp = sorted(nums)
    return binary_search_sorted(temp, target)


def jump_search(nums: [int], target: int, step: Optional[int] = None) -> int:
    n = len(nums)
    if step is None:
        step = math.sqrt(n)
    prev = 0
    while nums[int(min(step, n) - 1)] < target:
        prev = step
        step += step
        if prev >= n:
            return -1
    while nums[int(prev)] < target:
        prev += 1
        if prev == min(step, n):
            return -1
    if nums[int(prev)] == target:
        return prev
    return -1


def interpolation_search(nums: [int], target: int, l, r):
    """
    General equation of line : y = m*x + c.
    y is the value in the array and x is its index.

    Now putting value of lo,hi and x in the equation
    arr[hi] = m*hi+c ----(1)
    arr[lo] = m*lo+c ----(2)
    x = m*pos + c     ----(3)

    m = (arr[hi] - arr[lo] )/ (hi - lo)

    subtracting eqxn (2) from (3)
    x - arr[lo] = m * (pos - lo)
    lo + (x - arr[lo])/m = pos
    pos = lo + (x - arr[lo]) *(hi - lo)/(arr[hi] - arr[lo])
    """
    if l <= r and nums[l] <= target <= nums[r]:
        pos = l + ((r - l) // (nums[r] - nums[l]) * (target - nums[l]))
        if nums[pos] == target:
            return pos
        elif nums[pos] > target:
            return interpolation_search(nums, target, pos + 1, r)
        else:
            return interpolation_search(nums, target, l, pos - 1)
    return -1


# should be sorted useful in un-bounded search
def exponential_search(nums: [int], target: int) -> int:
    if nums[0] == target:
        return 0
    i = 1
    while i < len(nums) and nums[i] <= x:
        i *= 2
    return binary_search_sorted(nums[i // 2: min(i, len(nums) - 1) + 1], target)


if __name__ == '__main__':
    inp = [10, 2, 3, 5, 7, -1]
    t = -1
    print(linear_search(inp, t))
    print(binary_search_unsorted(inp, t))
    inp = [-1, 2, 3, 5, 7, 10]
    print(binary_search_sorted(inp, 5))
    print(jump_search(inp, t))
    print(interpolation_search(inp, t, 0, len(inp) - 1))
    print(exponential_search(inp, t))
